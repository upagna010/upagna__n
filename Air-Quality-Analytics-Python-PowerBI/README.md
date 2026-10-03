# 🌿 Smart Air Quality Intelligence System | Python + PowerBI

> Production-grade End-to-End Data Engineering & Analytics Project for Hyderabad Air Quality Monitoring

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![PowerBI](https://img.shields.io/badge/PowerBI-Dashboard-F2C811?style=for-the-badge&logo=powerbi)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql)

### 📌 Overview
An automated pipeline that fetches **real-time air pollution data** from **OpenAQ API**, cleans & transforms it using **Pandas**, loads it into **MySQL & CSV**, and visualizes actionable insights in **PowerBI**. Built for **Data Analyst / Data Engineer interviews**.

This project demonstrates **API Ingestion, Data Cleaning, Database Loading, and Business Intelligence** - end to end.

### 🏗️ Architecture
OpenAQ API (Real-time) → Python Ingestion (api_collection.py) → 
Data Cleaning (Pandas) → Storage (MySQL + CSV) → PowerBI Dashboard → Insightsjavascript
### 📁 Project Structure (Industry Standard)Air-Quality-Analytics-Python-PowerBI/
├── src/
│   └── Smart_Air_Quality_Intelligence_System/
│       ├── init.py
│       ├── api_collection.py    # Fetches data from OpenAQ v3 & v2 fallback
│       ├── db_loader.py         # MySQL + CSV loader
│       └── main.py              # Pipeline orchestrator
├── outputs/
│   ├── Smart_Air_quality_intelligence_cleaned.csv
│   └── Dashboard.pbix
├── Dashboard_image_screenshot.png
├── .env.example                 # Environment template
├── pyproject.toml               # Production packaging
├── requirements.txt
└── README.mdjavascript
### 🚀 Key Features
- ✅ **Real API with Fallback Logic** - Tries OpenAQ v3, auto-fallback to v2
- ✅ **Production Error Handling & Logging**
- ✅ **AQI Categorization** - Good / Moderate / Unhealthy logic
- ✅ **Dual Storage** - CSV for PowerBI + MySQL for production
- ✅ **.env Config Management** - Secure credential handling
- ✅ **PowerBI Interactive Dashboard**

### 📊 PowerBI Dashboard Insights
### 📸 Dashboard Preview
![Dashboard Screenshot](Dashboard_image_screenshot.png)
- City-wise **PM2.5 / PM10** pollution levels
- **AQI Category** distribution (Good, Moderate, Unhealthy)
- **Hyderabad Hotspots** - Most polluted areas
- Time-series trend analysis

### 🛠️ Tech Stack
- **Python**: Requests, Pandas, SQLAlchemy
- **Database**: MySQL
- **BI**: PowerBI
- **Tools**: python-dotenv, Logging

### ⚙️ How to Run (2 mins)
```bash
# 1. Clone repo
git clone https://github.com/upagna010/upagna_n.git
cd upagna_n/Air-Quality-Analytics-Python-PowerBI

# 2. Create virtual env
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt

# 3. Setup env
copy .env.example .env  # Add your DB credentials

# 4. Run pipeline
python main.py

# 5. Open Dashboard.pbix in PowerBI

🔮 Future EnhancementsAirflow orchestration for daily auto-runStreamlit live web appML prediction for next day AQI👩‍💻 AuthorUpagna Tulasala
Aspiring Data Analyst | Data Engineer | Python Developer
📍 Hyderabad, India
🔗 GitHub: @upagna010
