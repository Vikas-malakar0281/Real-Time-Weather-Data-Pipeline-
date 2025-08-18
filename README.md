# Real-Time Weather Data Pipeline 2025 🌦️

A real-time weather data streaming pipeline built with **Python**, **Apache Kafka**, **Apache Spark Streaming**, and **Docker** to process continuously changing weather conditions from Indian cities using the **Ambee Weather API**.  

This project **ingests, processes, and stores live weather and air quality data** for analytics and visualization (e.g., Power BI / Grafana), and is designed to be **scalable, modular, and fault-tolerant**.  

---

## 📝 About The Project

- **Project Name:** Real-Time Weather Data Pipeline 2025  
- **Objective:** To build a real-time, reliable data pipeline for weather and air quality monitoring.  
- **Current Status:**  
  - Project planning and roadmap setup in **Notion**  
  - API integration completed: fetching real-time weather and air quality data from [Ambee API](https://www.getambee.com/)  
  - Live project tracking available in Notion: [Project Plan & Progress](https://rainy-pirate-abe.notion.site/Real-Time-Weather-Pipeline-2025-24cc89a3b3b880b0b70ec4f59ac123a1)  
- **Progress According to Notion Template:**  
  - ✅ Project Planning & Roadmap  
  - ✅ API Integration  
  - ⏳ Kafka + Spark Streaming Pipeline (in progress)  
  - ⏳ Data Storage & Processing  
  - ⏳ Dashboard Visualization  
- **Estimated Completion:** [Insert Expected Date Based on Your Timeline]  

---

## 🚀 Features

- Real-time ingestion from Ambee Weather API  
- Streaming processing using Apache Kafka & Spark  
- Dockerized environment for quick setup & deployment  
- Scalable & fault-tolerant architecture  
- Stores processed data for analytics & visualization  
- Modular design to easily integrate additional APIs or cities  

---

## 🏗️ Pipeline Architecture
Ambee API → Kafka Producer → Kafka Topic → Spark Streaming → PostgreSQL / Data Lake → Visualization Dashboard

![Pipeline Architecture](docs/pipeline-diagram.png)  <!-- Add your diagram in /docs -->

---

## 🛠️ Tech Stack

- **Languages:** Python  
- **Streaming:** Apache Kafka, Spark Streaming  
- **Database:** PostgreSQL / Data Lake  
- **Visualization:** Power BI / Grafana  
- **Deployment:** Docker & Docker Compose  

---

## ⚡ Quick Start

1️⃣ **Clone the Repository**
```bash
git clone https://github.com/Vikas-malakar0281/Real-Time-Weather-Pipeline-2025.git
cd Real-Time-Weather-Pipeline-2025
```
2️⃣ Configure Environment Variables
Create a .env file in the project root:
```
AMBEE_API_KEY=your_api_key_here
KAFKA_BROKER=localhost:9092
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=weatherdb
```

3️⃣ Start the Pipeline
```
docker-compose up
```

4️⃣ View the Data
Connect Power BI / Grafana to the PostgreSQL database to visualize real-time analytics.


🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for improvements or new features.

📜 License

This project is licensed under the MIT License – see the LICENSE file for details.

👨‍💻 Author

Vikas Malakar
📧 malakarvikas738@gmail.com
🔗 LinkedIn | GitHub
