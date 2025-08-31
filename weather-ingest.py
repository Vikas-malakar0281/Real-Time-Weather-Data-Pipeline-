import os
import time
import json
import requests
import schedule
import pandas as pd
from dotenv import load_dotenv
from kafka import KafkaProducer, errors

# ----------------------------------
# 1. Load Environment Variables
# ----------------------------------
load_dotenv()

API_KEY = os.getenv("AMBEE_API_KEY")
CITIES_FILE = os.getenv("CITY_FILE")
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9094")  # Default local
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "weather_data")

# Validate essential configs
if not API_KEY:
    raise ValueError("❌ Missing AMBEE_API_KEY in .env")
if not os.path.exists(CITIES_FILE):
    raise FileNotFoundError(f"❌ Cities file not found: {CITIES_FILE}")

print(f"🔌 Connecting to Kafka broker at {KAFKA_BROKER}")
print(f"📂 Loading cities from {CITIES_FILE}")

# ----------------------------------
# 2. Initialize Kafka Producer
# ----------------------------------
producer = None
max_retries = 10
attempt = 0

while producer is None and attempt < max_retries:
    attempt += 1
    try:
        print(f"🔌 Attempt {attempt}/{max_retries}: Connecting to Kafka broker at {KAFKA_BROKER} ...")
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BROKER,
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )
        print("✅ Connected to Kafka broker!")
    except errors.NoBrokersAvailable:
        print(f"⚠️ Broker not available (attempt {attempt}). Retrying in 5 seconds...")
        time.sleep(5)

if producer is None:
    raise RuntimeError(f"❌ Failed to connect to Kafka broker {KAFKA_BROKER} after {max_retries} attempts.")

# ----------------------------------
# 3. Load Cities
# ----------------------------------
df_cities = pd.read_csv(CITIES_FILE)  # Must contain: city, lat, lng
required_columns = {"city", "lat", "lng"}
if not required_columns.issubset(df_cities.columns):
    raise ValueError(f"❌ Cities file must contain columns: {required_columns}")

# ----------------------------------
# 4. Fetch Weather Function
# ----------------------------------
def get_weather(lat: float, lng: float) -> dict | None:
    """Fetch weather data from Ambee API for given coordinates."""
    url = f"https://api.ambeedata.com/weather/latest/by-lat-lng?lat={lat}&lng={lng}"
    headers = {
        "x-api-key": API_KEY,
        "Content-type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed for ({lat}, {lng}): {e}")
        return None

# ----------------------------------
# 5. Main Loop - Send Weather Data to Kafka
# ----------------------------------
for _, row in df_cities.iterrows():
    city_name = row["city"]
    print(f"🌍 Fetching data for {city_name} (lat={row['lat']}, lng={row['lng']}) ...")

    weather_data = get_weather(row["lat"], row["lng"])
    if weather_data:
        record = {"city": city_name, "data": weather_data}
        try:
            producer.send(KAFKA_TOPIC, record)
            print(f"✅ Sent to Kafka topic '{KAFKA_TOPIC}': {record}")
        except Exception as e:
            print(f"❌ Failed to send record for {city_name}: {e}")

    time.sleep(1)  # Respect API rate limits

# ----------------------------------
# 6. Cleanup
# ----------------------------------
print("🚀 Flushing and closing Kafka producer...")
producer.flush()
producer.close()
print("✅ Weather ingestion completed.")

# ------------------------------------
# 7. Schedule
# ------------------------------------
schedule.every(1).hours.do(get_weather)

print("⏳ Weather ingestion service started...")

while True:
    schedule.run_pending()
    time.sleep(1)