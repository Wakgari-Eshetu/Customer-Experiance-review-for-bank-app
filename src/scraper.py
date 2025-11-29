from google_play_scraper import reviews, Sort
import pandas as pd

class PlayStoreScraper:
    def __init__(self, app_id, bank_name, source):
        self.app_id = app_id
        self.bank_name = bank_name
        self.source = source

    def scrape(self, count=400):
        result, _ = reviews(
            self.app_id,
            lang="en",
            country="et",
            sort=Sort.NEWEST,
            count=count
        )

        df = pd.DataFrame(result)
        df = df[['content', 'score', 'at']]
        df.columns = ['review', 'rating', 'date']

        df['bank'] = self.bank_name
        df['source'] = self.source

        return df

    def save_raw(self, df):
        filename = self.bank_name.replace(" ", "_").lower() + ".csv"
        df.to_csv(f"data/raw/{filename}", index=False)
