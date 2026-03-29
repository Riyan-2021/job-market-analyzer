import pandas as pd
from scraper.freelance_scraper import scrape_freelance

def run_scraper():
    df = scrape_freelance()

    df.to_csv(
        "data/jobs.csv",
        index=False
    )

    print("Data Saved Successfully!")

if __name__ == "__main__":
    run_scraper()
