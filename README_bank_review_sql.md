# bank_review.sql — schema for storing bank apps and reviews

This file documents the SQL schema in `bank_review.sql` and provides instructions to create the schema in a target database. The provided SQL in the repository is written for PostgreSQL.

Location
- SQL file: `bank_review.sql` (root of repository)

Schema overview
- `banks` table: stores bank metadata (bank_id, bank_name, app_name)
- `reviews` table: stores user reviews with a foreign key to `banks` and fields such as rating, review_date, sentiment_label, and sentiment_score.

PostgreSQL (recommended) — how to run
1. Ensure Postgres is running and you have a database (e.g., `bank_reviews`):
```powershell
psql -U postgres -c "CREATE DATABASE bank_reviews;"
```
2. Run the schema file:
```powershell
psql -U postgres -d bank_reviews -f bank_review.sql
```

Notes for compatibility with other engines
- MySQL: replace `SERIAL` with `INT AUTO_INCREMENT` and ensure `InnoDB` engine for foreign keys. Example adjustment in MySQL:
```sql
CREATE TABLE banks (
  bank_id INT AUTO_INCREMENT PRIMARY KEY,
  bank_name VARCHAR(255) NOT NULL,
  app_name VARCHAR(255)
);
```

- SQLite: use `INTEGER PRIMARY KEY AUTOINCREMENT` and enable foreign keys with `PRAGMA foreign_keys = ON;` before creating tables. Date columns in SQLite are usually stored as `TEXT` in ISO format.

Recommended improvements to `bank_review.sql`
- Add `IF NOT EXISTS` to `CREATE TABLE` statements to avoid errors when tables already exist.
- Add a `UNIQUE` constraint on `banks(bank_name)` if you rely on `ON CONFLICT (bank_name) DO NOTHING` semantics.
- Example safe Postgres schema snippet:
```sql
CREATE TABLE IF NOT EXISTS banks (
  bank_id SERIAL PRIMARY KEY,
  bank_name VARCHAR(255) NOT NULL UNIQUE,
  app_name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS reviews (
  review_id SERIAL PRIMARY KEY,
  bank_id INT REFERENCES banks(bank_id) ON DELETE CASCADE,
  review_text TEXT NOT NULL,
  rating INT CHECK (rating >= 0 AND rating <= 5),
  review_date DATE,
  sentiment_label VARCHAR(50),
  sentiment_score FLOAT,
  source VARCHAR(100)
);
```

Verifying the schema
- Connect to the DB and run:
```sql
\dt   -- list tables (psql)
SELECT column_name, data_type FROM information_schema.columns WHERE table_name='reviews';
```

Troubleshooting common errors
- "Incorrect syntax near '30 days'": this comes from using `INTERVAL '30 days'` (Postgres syntax) in a non-Postgres engine such as SQL Server. Use the engine-appropriate date arithmetic (e.g., `DATEADD(day, -30, GETDATE())` for T-SQL).
- Foreign key errors in SQLite: ensure `PRAGMA foreign_keys = ON;` is set before creating tables.
- Table already exists: run `CREATE TABLE IF NOT EXISTS` or drop the table before creating during development.

If you'd like, I can:
- Patch `bank_review.sql` to include `IF NOT EXISTS` and the `UNIQUE` constraint on `bank_name` and commit the change. 
- Create alternate versions for MySQL/SQLite (e.g., `bank_review_mysql.sql`, `bank_review_sqlite.sql`).
