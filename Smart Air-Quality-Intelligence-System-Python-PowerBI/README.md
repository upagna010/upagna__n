# 🌿 Smart Air-Quality-Intelligence-System - Python & Power BI

### 📌 Overview
An end-to-end Data Analytics project that collects real-time Air Quality data via API, cleans it using Python, and visualizes pollution trends & health risks through an interactive Power BI dashboard.

### 🎯 Problem Statement
Air pollution is increasing in Indian cities. The goal is to monitor AQI levels (PM2.5, PM10, AQI) and provide health-based insights for citizens.

### 🔄 Project Workflow / Architecture
1.  **Data Collection:** `api_collection.py` - Fetched real-time AQI data from API
2.  **Data Loading & Automation:** `db_loader.py` + `main.py` - Automated data ingestion pipeline
3.  **Data Cleaning:** `Smart_Air_quality_intelligence_cleaned.csv` - Cleaned using Pandas (handled nulls, duplicates)
4.  **Data Visualization:** `Dashboard.pbix` - Built interactive dashboard in Power BI

### 📁 Files in this Repository
- `api_collection.py` - Script for API data collection
- `db_loader.py` - Loads data into database/storage
- `main.py` - Main runner file
- `Smart_Air_quality_intelligence_cleaned.csv` - Final cleaned dataset
- `Dashboard.pbix` - Power BI dashboard file
- `Dashboard_image_screenshot.png` - Dashboard preview
- `.env.example` - Sample env file for API keys
- `pyproject.toml` - Project dependencies

### 🛠️ Tech Stack
- **Python:** Pandas, Requests
- **API Integration:** OpenWeather / AQI API
- **Visualization:** Power BI, DAX
- **Tools:** GitHub, Excel

### 📊 Dashboard Features
- City-wise AQI comparison
- PM2.5 vs PM10 trend analysis
- Health Risk Category (Good, Moderate, Unhealthy)
- Time-series pollution trends

### 🚀 How to Run
1. Clone repo: `git clone ...`
2. Install requirements from `pyproject.toml`
3. Add API key in `.env`
4. Run `python main.py`
5. Open `Dashboard.pbix` in Power BI Desktop

### 💡 Key Insights
- Found PM2.5 is the major pollutant in top 3 cities
- Identified peak pollution hours (8AM & 8PM)
- Categorized health risk zones for citizens

### 🔮 Future Scope
- Add predictive model for AQI forecasting
- Add automated email alerts for high AQI

---
**Author:** Upagna 
