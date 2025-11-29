# Customer Experience Review for Bank App

An open-source Python project to collect, preprocess, and analyze mobile app reviews for multiple Ethiopian bank apps from the Google Play Store. Use it to gather user feedback, run NLP-based sentiment and thematic analysis, and explore the cleaned dataset with notebooks.

---

## 🚀 Project Overview
- Purpose: Scrape user reviews for selected bank apps from Google Play Store, clean and preprocess the text, perform sentiment analysis and thematic clustering, and provide analysis-ready CSVs and exploratory visualizations.
- Key features:
	- Play Store scraping via `google_play_scraper` (saves raw CSVs)
	- Preprocessing: deduplication, missing value handling, date normalization, text cleaning
	- Sentiment analysis: DistilBERT or VADER fallback options
	- Thematic analysis: TF-IDF + clustering and keyword extraction
	- Jupyter notebooks for EDA and visualization

## 🗂️ Repository Structure
```
main.py                       # Orchestrator: scrape and preprocess (Task 1)
requirements.txt              # Project dependencies
README.md                     # Project documentation (this file)
data/
	├─ raw/                     # Raw CSVs saved by scraper
	└─ processed/               # Clean/processed CSVs used for analysis
notebook/
	├─ EDAfor task1.ipynb       # EDA and cleaning pipeline
	├─ task-2.ipynb             # Sentiment + thematic analysis notebook
	└─ visualtask-2.ipynb       # Additional visualizations
src/
	├─ config.py                # App IDs and constants
	├─ scraper.py               # Play Store scraping
	└─ preprocessor.py          # Data cleaning and preprocessing
```

## 🧰 Dependencies
Core dependencies are listed in `requirements.txt`. The primary libraries used are:

- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- nltk
- wordcloud
- google_play_scraper
- transformers (Hugging Face)
- torch (PyTorch)
- vaderSentiment
- jupyterlab

Optional/extended packages: `plotly`, `gensim`, etc. See `requirements.txt` for suggested minimum versions.

## ⚙️ Installation & Setup
1. (Optional but recommended) Create and activate a virtual environment (Windows PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
2. Upgrade pip and install dependencies:
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. (Optional) If you want to install PyTorch with a specific build (CUDA support) see https://pytorch.org/ for correct wheel selection. For CPU-only:
```powershell
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

4. Download NLTK data (stopwords used in notebooks):
```powershell
python -c "import nltk; nltk.download('stopwords')"
```

## ▶️ How to Run
1. Scrape and preprocess reviews (Task 1):
```powershell
python main.py
```
This will:
- Scrape reviews using `src/scraper.py` and save raw CSVs to `data/raw/`.
- Concatenate and preprocess reviews, saving the cleaned CSV `data/processed/clean_reviews.csv`.

2. Run EDA or Task 2 analysis via Jupyter:
```powershell
jupyter lab notebook/EDAfor\ task1.ipynb
# or
jupyter lab notebook/task-2.ipynb
```

3. If you use the HuggingFace models (transformers), the notebooks include commands to install `transformers` and `torch`. The transformer model loads may take time based on connectivity and hardware.

## 🔎 Notes & Tips
- The `google_play_scraper` uses Play Store and may return limited results per country. Adjust `country` or `count` in `src/scraper.py` as needed.
- When using GPU-friendly PyTorch, set the `device` parameter (0, 1, etc.) in the transformer pipeline constructors.
- Some transformers-based models may require a lot of RAM or a GPU for faster processing; consider using smaller batch sizes on CPU.

## 🧪 Tests & Development
- This repo doesn't yet include unit tests; please add tests for `src.scraper` and `src.preprocessor` if you expand or refactor behavior.

## 🤝 Contributing
Contributions welcome — please open a GitHub issue or pull request for major changes. Include a short description of your changes and add tests where possible.

## 📝 License
Add a `LICENSE` file to explicitly declare reuse/redistribution permissions (e.g., MIT or Apache-2.0).

## Contact
Wakgari Eshetu — lelikenakoo663@gmail.com

---
If you want, I can:
- Add a `Makefile` or PowerShell script for common tasks (setup, run main, start notebooks).
- Add a GitHub Action to enforce linting (flake8) or run simple tests.
- Add instructions for installing PyTorch for GPU with specific CUDA versions.

Tell me which you'd like and I'll add it.
