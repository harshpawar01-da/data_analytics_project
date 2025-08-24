# 🌏 Mumbai Air Quality Analytics Project

## 📌 Overview
This project analyzes **Mumbai’s air quality** using open datasets.  
It demonstrates **end-to-end data analytics skills** – from **data cleaning** to **exploratory analysis**, **SQL insights**, **time-series forecasting**, and **dashboard storytelling**.  

The aim is to show how **data analysis can support real-world decisions** for:
- Urban planning & policy makers  
- Healthcare & insurance  
- Environmental NGOs  
- Businesses (e.g., air purifier companies, tourism, logistics)  

---

## 🗂️ Project Structure
mumbai-air-quality-analytics/
│── data/
│ ├── raw/ # Original dataset
│ ├── processed/ # Cleaned & transformed data
│
│── notebooks/
│ ├── 01_exploratory_analysis.ipynb
│ ├── 02_modeling_forecasting.ipynb
│
│── scripts/
│ ├── build_features.py # Feature engineering
│ ├── plots.py # Reusable visualization functions
│
│── sql/
│ ├── examples.sql # SQL queries for insights
│
│── dashboard/
│ ├── powerbi_dashboard.pbix # Power BI dashboard file
│ ├── tableau_dashboard.twbx # Tableau dashboard file
│
│── README.md



---

## ⚙️ Setup Instructions

1. **Clone Repository**
```bash
git clone https://github.com/yourusername/mumbai-air-quality-analytics.git
cd mumbai-air-quality-analytics

2. Create Virtual Environment & Install Dependencies
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt

3. Data Preparation
Place raw dataset in data/raw/
Run feature engineering:
python scripts/build_features.py
This will generate data/processed/mumbai_air_quality_clean.csv

4.Run Notebooks
01_exploratory_analysis.ipynb → Data cleaning, summary stats, EDA, and visualizations
02_modeling_forecasting.ipynb → ARIMA/Prophet forecasting, business insights

5.SQL Analytics
Open sql/examples.sql in SQLite/Postgres/MySQL and run queries for extra insights

6.Dashboard
Open dashboard/powerbi_dashboard.pbix or dashboard/tableau_dashboard.twbx
Interactive view of air quality trends, hotspots, and health risk zones


Key Features
✅ Data Cleaning & Preprocessing
✅ Feature Engineering (weekend flag, pollution categories, AQI grouping)
✅ Exploratory Data Analysis (heatmaps, trends, station-wise comparisons)
✅ SQL Analytics for querying trends & KPIs
✅ Forecasting Models (ARIMA, Prophet) to predict future PM2.5 levels
✅ Interactive Dashboards (Power BI / Tableau)
✅ Business Recommendations

Business Impact
📌 Healthcare: Forecasts help hospitals prepare for higher patient loads (respiratory issues).
📌 Government: Early warnings for dangerous pollution levels aid policy & regulation.
📌 Businesses: Air purifier & healthcare product companies can plan inventory.
📌 Citizens: Dashboards inform safer outdoor activity times.



Tech Stack
Python (pandas, numpy, matplotlib, seaborn, statsmodels, prophet)
SQL (SQLite/Postgres/MySQL for queries)
Dashboards: Power BI / Tableau
Jupyter Notebooks for analysis



👨‍💻 Author
Harsh P.
Data Analyst | Skilled in SQL, Python, Visualization, Business Analytics