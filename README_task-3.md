# Task 3 — Insert Cleaned Reviews into PostgreSQL

This document describes how to run the Task‑3 Python notebook (`notebook/task-3.ipynb`) which loads the cleaned reviews CSV and inserts rows into a PostgreSQL database.

Location
- Notebook: `notebook/task-3.ipynb`
- Uses: `data/processed/clean_reviews.csv` and SQL schema `bank_review.sql`

Purpose
- Load the cleaned reviews produced in Task 1 and persist them into a Postgres database so downstream analysis and queries can be performed.

Prerequisites
- Python 3.8+ and a virtual environment (recommended)
- `pip install -r requirements.txt` (note: install `psycopg2-binary` if you run Task 3 as a script)
- A running PostgreSQL server and a database named `bank_reviews` (or update connection parameters in the notebook)

Required Python packages (not exhaustive)
- pandas
- psycopg2-binary  (use `pip install psycopg2-binary`)

Setup Steps
1. Create and activate a virtual env (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
2. Install project dependencies and `psycopg2-binary`:
```powershell
pip install -r requirements.txt
pip install psycopg2-binary
```
3. Create the Postgres database (if not present):
```powershell
# connect as a Postgres superuser and run:
psql -U postgres -c "CREATE DATABASE bank_reviews;"
```
4. Create the tables using the SQL schema (see `bank_review.sql`):
```powershell
psql -U postgres -d bank_reviews -f bank_review.sql
```

Configure connection
- The notebook uses a connection block with parameters such as `dbname`, `user`, `password`, `host`, and `port`. Update these in `notebook/task-3.ipynb` to match your environment. For production, store credentials in environment variables or a `.env` file and do not commit them.

Run Task 3
- Open the notebook and run the cells in order:
  1. Load `data/processed/clean_reviews.csv` and inspect
  2. Connect to Postgres using `psycopg2`
  3. Insert banks and reviews (the notebook uses `ON CONFLICT (bank_name) DO NOTHING` for dedup)
  4. Commit and verify insertion

Example: run the notebook via Jupyter Lab
```powershell
jupyter lab notebook/task-3.ipynb
```

Run as a script (optional)
- You can convert the notebook to a script and run it headless:
```powershell
jupyter nbconvert --to script notebook/task-3.ipynb
python notebook/task-3.py
```
Ensure the connection code in the generated script references environment variables or a secure config.

Troubleshooting
- "Incorrect syntax near '30 days'": this error is not from the notebook insertion script itself — it usually comes from running Postgres-style `INTERVAL '30 days'` in non-Postgres engines (SQL Server). Ensure you run `bank_review.sql` and other queries against PostgreSQL.
- Connection refused: verify Postgres is running and credentials are correct.
- Unique/constraint errors: the notebook uses an `INSERT INTO banks ... ON CONFLICT DO NOTHING` pattern; ensure the table has a `UNIQUE` or `PRIMARY KEY` constraint (banks.bank_name should be unique for that pattern to work reliably).

Next steps / Improvements
- Move DB credentials to environment variables or a `.env` and load them in the notebook.
- Convert notebook insertion logic into a reproducible Python script `scripts/load_reviews.py` and add CLI args for `--db`, `--user`, `--password`.
- Add unit tests that validate transformation and insertion for a small sample dataset.

If you want, I can create a `scripts/load_reviews.py` file and wire a simple CLI. Request that and I’ll implement it.
