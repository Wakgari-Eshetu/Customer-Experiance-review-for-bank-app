# Task 4 — Visualization & Quick Analysis (notebook/task-4.ipynb)

This README explains the purpose and usage of the Task 4 notebook located at `notebook/task-4.ipynb`. Task 4 pulls reviews from the `reviews` table, performs simple aggregations and visualizations, and saves charts into `outputs/`.

What Task 4 does
- Connects to a PostgreSQL database (`bank_reviews`) and reads review records via a JOIN between `reviews` and `banks`.
- Computes basic metrics:
  - Number of positive and negative reviews per bank
  - Average rating per bank
  - Rating distribution across all reviews
  - Keyword mention counts for a small keyword list (`crash`, `login`, `bug`, `error`, `transfer`)
- Produces visual outputs saved into `outputs/` (e.g., `sentiment_per_bank.png`, `rating_distribution.png`, `avg_rating_per_bank.png`).

Prerequisites
- `requirements.txt` should be installed in your environment. Key packages used in this notebook include:
  - `pandas`, `matplotlib`, `nltk`, `psycopg2-binary`, `wordcloud`, `scikit-learn` (if TF-IDF used)
- A running PostgreSQL instance with the `bank_reviews` database and the `banks` and `reviews` tables populated.

Setup
1. Create and activate a virtual environment (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
2. Install dependencies:
```powershell
pip install -r requirements.txt
pip install psycopg2-binary
```
3. Ensure NLTK stopwords are downloaded (the notebook downloads them automatically but you can run explicitly):
```powershell
python -c "import nltk; nltk.download('stopwords')"
```

Running the notebook
- Start Jupyter Lab or Notebook and open `notebook/task-4.ipynb`:
```powershell
jupyter lab notebook/task-4.ipynb
```
- Run cells in order. The notebook will create an `outputs/` directory (it calls `os.makedirs('outputs', exist_ok=True)`), save charts there, and print quick metrics to the notebook output.

Configuration
- The notebook connects to Postgres with connection values hardcoded in the notebook (dbname, user, password, host, port). For better security, replace those with environment variables or a small config module.

Files produced
- `outputs/sentiment_per_bank.png`
- `outputs/rating_distribution.png`
- `outputs/avg_rating_per_bank.png`

Notes & Suggestions
- Secure credentials: avoid hardcoding the DB password. Use environment variables or a `.env` file loaded via `python-dotenv`.
- Error: "Incorrect syntax near '30 days'" — This is unrelated to the notebook and comes from running Postgres interval syntax in a non-Postgres engine (or incorrect SQL elsewhere). Ensure you run the SQL against PostgreSQL.
- If the notebook fails to connect, verify Postgres is running and the credentials (host/port/user/password) are correct.
- Consider parameterizing queries (e.g., limit by time range) and saving the resulting `DataFrame` into `data/processed` for reproducible visualizations.

Next steps I can help with
- Replace hardcoded DB credentials with environment-variable-based config and update the notebook.
- Add more visualizations or export an HTML dashboard.
- Create a script `scripts/generate_reports.py` to run the notebook logic headless and produce outputs for scheduling.

If you want me to implement any of the next steps, tell me which and I will proceed.
