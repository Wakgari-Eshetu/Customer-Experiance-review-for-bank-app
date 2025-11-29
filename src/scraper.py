from google_play_scraper import reviews, Sort
import pandas as pd

class PlayStoreScraper:
    def __init__(self, app_id, bank_name, source):
        self.app_id = app_id
        self.bank_name = bank_name
        self.source = source

    def scrape(self, count=400):
        """Scrape reviews safely, handle missing keys or empty results."""
        try:
            result, _ = reviews(
                self.app_id,
                lang='en',
                country='et',  # or 'us' if no reviews in Ethiopia
                sort=Sort.NEWEST,
                count=count
            )

            if not result:
                print(f"No reviews found for {self.bank_name}")
                return pd.DataFrame(columns=['review','rating','date','bank','source'])

            df = pd.DataFrame(result)

            # Ensure expected columns exist
            for col in ['content', 'score', 'at']:
                if col not in df.columns:
                    df[col] = None

            df = df[['content', 'score', 'at']]
            df.columns = ['review', 'rating', 'date']
            df['bank'] = self.bank_name
            df['source'] = self.source

            return df

        except Exception as e:
            print(f"Error scraping {self.bank_name}: {e}")
            return pd.DataFrame(columns=['review','rating','date','bank','source'])

    def save_raw(self, df):
        filename = self.bank_name.replace(" ", "_").lower() + ".csv"
        df.to_csv(f"data/raw/{filename}", index=False)
