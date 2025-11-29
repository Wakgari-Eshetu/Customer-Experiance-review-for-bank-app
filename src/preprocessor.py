import pandas as pd

class ReviewPreprocessor:
    def __init__(self, df):
        self.df = df

    def remove_duplicates(self):
        self.df.drop_duplicates(subset="review", inplace=True)

    def handle_missing(self):
        self.df.dropna(subset=["review", "rating", "date"], inplace=True)

    def normalize_dates(self):
        self.df["date"] = pd.to_datetime(self.df["date"]).dt.date

    def preprocess(self):
        self.remove_duplicates()
        self.handle_missing()
        self.normalize_dates()
        return self.df

    def save_clean(self):
        self.df.to_csv("data/processed/clean_reviews.csv", index=False)
