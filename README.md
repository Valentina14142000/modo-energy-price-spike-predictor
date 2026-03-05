# ⚡ ERCOT Electricity Market Dashboard

An interactive dashboard for analyzing electricity demand, price behavior, and detecting price spikes in the ERCOT electricity market.

This project was built as part of the Modo Energy Open Technical Challenge.

---

## Problem

Electricity markets often experience extreme price volatility when demand approaches system limits. These price spikes can significantly impact traders, utilities, and asset operators.

Understanding **when price spikes occur and how demand influences price** is critical for market participants.

This project explores the relationship between **electricity demand and market prices** and provides a simple tool for detecting price spikes.

---

## What This Project Does

The dashboard:

• Visualizes electricity **demand over time**  
• Shows the relationship between **demand and price**  
• Detects **price spike events**  
• Displays key **market statistics**

The goal is to provide a quick way for market participants to understand price volatility conditions.

---

## Dashboard Features

### Demand Over Time
Displays electricity demand trends across time.

### Price vs Demand
Scatter plot showing the relationship between electricity demand and market prices.

### Price Spike Detection
Automatically identifies extreme price events based on the **95th percentile threshold**.

### Quick Statistics
Key indicators such as:

- Maximum price
- 95th percentile price
- Spike detection threshold

---

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- Plotly
- Streamlit

---

## Project Structure
valentina@MacBook-Air-Salavdi modo-energy-price-spike-predictor % tree
.
├── README.md
├── app.py
├── data
│   └── ercot_data.csv
├── requirements.txt
└── src
    ├── __pycache__
    │   └── analysis.cpython-312.pyc
    ├── analysis.py
    └── model.py

4 directories, 7 files