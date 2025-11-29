import pandas as pd
from src.scraper import PlayStoreScraper
from src.preprocessor import ReviewPreprocessor
from src.config import BANK_APPS, SOURCE

all_reviews = []

for bank, app_id in BANK_APPS.items():
    scraper = PlayStoreScraper(app_id, bank, SOURCE)
    df = scraper.scrape(count=400)
    scraper.save_raw(df)
    all_reviews.append(df)

# Merge all banks
df_all = pd.concat(all_reviews, ignore_index=True)

# Preprocess
processor = ReviewPreprocessor(df_all)
df_clean = processor.preprocess()
processor.save_clean()

print("Task 1 completed successfully!")
print("Total Reviews:", len(df_clean))
