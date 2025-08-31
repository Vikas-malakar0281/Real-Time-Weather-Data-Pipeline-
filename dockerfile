FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY weather-ingest.py .
COPY cities.csv .
COPY .env .

# Default command to run the script
CMD ["python", "weather-ingest.py"]
