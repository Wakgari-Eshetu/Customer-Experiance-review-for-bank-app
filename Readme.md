# Customer Experience Review for Bank App

A simple Python project to collect, preprocess, and analyze mobile app reviews for bank apps (Google Play Store). This repository includes a small scraper for Play Store reviews, preprocessing utilities, and an EDA notebook to examine the data.

---

## 🚀 Project Overview
- Purpose: Gather user feedback from Google Play Store for a set of Ethiopian bank apps, clean and prepare the reviews, and provide an analysis-ready dataset for exploratory data analysis and modeling.
- Primary components: scraping (Play Store), preprocessing (cleaning and transformation), and an exploratory Jupyter notebook for analysis.

## 🗂️ Repository Structure
```
main.py                       # Entry point: scrape and preprocess reviews
requirements.txt              # Required packages (add packages here or see Install)
README.md                     # Project readme (this file)
data/
	└─ raw/                     # Raw CSVs saved by scraper
	└─ processed/               # Clean/processed CSVs used for analysis
notebook/
	└─ EDAfor task1.ipynb       # Jupyter notebook for EDA
src/
	├─ config.py                # App IDs and sources configuration
	├─ scraper.py               # Play Store scraping logic
	└─ preprocessor.py          # Data cleaning and preprocessing
```

## 🧰 Key Files
- `main.py` - Orchestrates scraping and preprocessing. Uses `src/config.py` values to know which apps to scrape.
- `src/scraper.py` - Uses the `google_play_scraper` package to pull reviews and save raw CSVs under `data/raw/`.
- `src/preprocessor.py` - Cleans data, removes duplicates, handles missing values, and normalizes dates.
- `notebook/EDAfor task1.ipynb` - Exploratory analysis of the cleaned dataset.

## ⚙️ Installation & Setup
1. (Optional but recommended) Create and activate a virtual environment (Windows PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
2. Install required packages. The repository may not yet list dependencies in `requirements.txt`. Suggested install commands:
```powershell
pip install pandas google_play_scraper jupyterlab
```
If you maintain `requirements.txt`, add:
```
pandas
google_play_scraper
jupyterlab
```

3. Ensure data directories exist before running the scraper:
```powershell
mkdir -Force data\raw; mkdir -Force data\processed
```

## ▶️ How to Use
1. Configure which apps to scrape and the source in `src/config.py`. The default includes 3 banks:
```python
BANK_APPS = {
		"Commercial Bank of Ethiopia": "com.combanketh.mobilebanking",
		"Bank of Abyssinia": "com.boa.mobilebanking",
		"Dashen Bank": "com.dashen.mobile"
}
SOURCE = "Google Play Store"
```

2. Run the main script to scrape reviews and generate a cleaned CSV:
```powershell
python main.py
```
This will:
- Scrape up to the `count` number of reviews for each app (the default in `main.py` uses `count=400`).
- Save separate raw CSVs into `data/raw/`.
- Concatenate all reviews, preprocess them using `src/preprocessor.py`, and save a clean CSV at `data/processed/clean_reviews.csv`.

3. Explore the data using the Jupyter notebook:
```powershell
jupyter lab notebook/EDAfor\ task1.ipynb
```

## 🔎 Notes & Tips
- The `google_play_scraper` package returns a list of reviews — country and language can be set for the `reviews()` call. If reviews for `country='et'` are sparse, consider `country='us'`.
- If the Play Store changes structure or rate limits, scraping may fail; consider running with smaller `count` or adding delay logic to the scraper.
- This project currently saves CSVs locally; if you intend to scale or run on a CI/CD platform, consider object storage or database options.

## 📂 Data
- Raw CSVs (one per bank) are saved into `data/raw/` by `src/scraper.py`.
- Cleaned reviews CSV is saved as `data/processed/clean_reviews.csv` by `src/preprocessor.py`.

## 🤝 Contributing
Contributions are welcome. To propose a change:
1. Fork the repo.
2. Create a feature branch.
3. Submit a pull request with a clear description of changes.

## 📝 License
This project currently does not include an explicit license; add a `LICENSE` file if you want to define reuse rules (e.g., MIT, Apache 2.0, etc.).

## 👤 Author
Wakgari Eshetu

---
💡 If you want, I can also:
- Add a `requirements.txt` file with pinned package versions.
- Add GitHub Actions to run a basic test (like linting).
- Improve `main.py` to accept CLI arguments to configure the scrape count or which banks to run.

If you'd like any of those, tell me which one and I’ll implement it!
