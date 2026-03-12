# 📘 market-data-usage-analyser

A clean, portfolio‑ready project for analysing market‑data usage logs using Python.

## 📁 Project Structure

market-data-usage-analyser/
│
├── data/
│   └── usage_log.csv
│
├── src/
│   └── analyse_usage.py
│
├── tests/
│   └── test_basic.py
│
└── README.md

## 📄 Dataset Overview

The dataset (usage_log.csv) contains 50 lines of realistic, fictional market‑data usage events. Each row represents a single consumption event.

Example row:
2024‑11‑12T09:15:26Z, AKHAN, IDN, AAPL.O, 55, 22100, US‑EQ‑L1

Columns:
- timestamp: Event time (UTC)
- user_id: User consuming data
- service: Market‑data service (e.g., IDN, BBG_PROD)
- ric: Instrument (e.g., AAPL.O, EURUSD=)
- msg_count: Number of messages consumed
- bytes: Total bytes consumed
- entitlement: Entitlement level

## 🌐 What the Script Does

The analysis script (analyse_usage.py) performs:
- Loading and parsing the usage log
- Cleaning and normalising string fields
- Computing useful metrics:
  - total messages per user
  - total bytes per user
  - most active instruments
  - usage per service
  - peak usage periods
- Printing a summary to the terminal
- (Future) exporting results to CSV/JSON

The project is intentionally modular so it can grow into a more advanced tool.

## 🚀 How to Run the Script

1. Install dependencies:
   pip install -r requirements.txt

2. Run the analysis:
   python src/analyse_usage.py

(As the project evolves, this may become a CLI tool with arguments.)

## 🧪 Tests

A minimal test suite validates:
- the dataset loads correctly
- required columns exist
- basic aggregations run without errors

Tests can be expanded as the project grows.

## 🛠️ Future Enhancements

Planned improvements:
- CLI arguments (--input, --output, --format)
- Export results to CSV/JSON
- Parquet output for downstream analytics
- Visualisations (matplotlib or seaborn)
- Anomaly detection (spikes, unusual instruments)
- Entitlement mismatch checks
- Multi‑day dataset support

## 📌 Purpose

This project demonstrates:
- Python data analysis
- Market‑data domain knowledge
- Log parsing
- Engineering structure
- Reproducible workflows

It is not based on any real client or proprietary data.

