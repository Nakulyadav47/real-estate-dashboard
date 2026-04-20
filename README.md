# 📊 Real Estate Growth Prediction Dashboard

## 🚀 Overview
This project is a simple AI-based dashboard that predicts high-growth real estate areas using key factors like price, rent, and listing density.

## 🧠 Features
- Dynamic CSV file upload
- Weighted Growth Score calculation
- Interactive filtering by area
- Data visualization using charts

## ⚙️ Tech Stack
- Python
- Pandas
- Streamlit

## 📈 Logic
The system calculates a Growth Score using a weighted formula:
Growth Score = 0.5 * Price + 0.3 * Rent + 0.2 * Listings

This helps identify top-performing areas for investment.

## ▶️ How to Run
```bash
pip install pandas streamlit
python -m streamlit run app.py
