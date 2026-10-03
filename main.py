import logging
from .api_collection import fetch_air_quality
from .db_loader import load_to_sql, save_csv

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def run(city="Hyderabad"):
    logging.info(f"Starting pipeline for {city}")
    df = fetch_air_quality(city=city)
    if not df.empty:
        save_csv(df)
        load_to_sql(df)
        logging.info("Pipeline completed successfully")
    else:
        logging.warning("No data fetched")
    return df

if __name__ == "__main__":
    run()