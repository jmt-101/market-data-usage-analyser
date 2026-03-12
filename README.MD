📂 Project Structure


📄 Dataset Overview
The dataset () contains 50 lines of realistic, fictional market‑data usage events.
Each row represents a single consumption event:

Example row:


🎯 What the Script Does
The analysis script () will:
• 	Load the usage log
• 	Clean and normalise the data
• 	Compute useful metrics such as:
• 	total messages per user
• 	total bytes per user
• 	most active instruments
• 	usage per service
• 	peak usage periods
• 	Output a summary to the terminal (and optionally to CSV/JSON later)
This project is intentionally modular so it can grow into a more advanced tool.

🚀 How to Run the Script
Install dependencies:

Run the analysis:

(As the project evolves, this may become a CLI tool with arguments.)

🧪 Tests
A minimal test suite is included to validate:
• 	the dataset loads correctly
• 	required columns exist
• 	basic aggregations run without errors
Tests can be expanded as the project grows.

🛠️ Future Enhancements
Planned improvements:
• 	CLI arguments (, , )
• 	Export results to CSV/JSON
• 	Parquet output for downstream analytics
• 	Visualisations (matplotlib or seaborn)
• 	Anomaly detection (spikes, unusual instruments)
• 	Entitlement mismatch checks
• 	Multi‑day dataset support

📌 Purpose
This project is designed as a portfolio‑ready demonstration of:
• 	Python data analysis
• 	market‑data domain knowledge
• 	log parsing
• 	engineering structure
• 	reproducible workflows
It is not based on any real client or proprietary data.