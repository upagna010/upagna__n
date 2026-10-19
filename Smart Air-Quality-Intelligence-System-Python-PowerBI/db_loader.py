import pandas as pd
import sqlite3
from pathlib import Path
import logging

logger = logging.getLogger(__name__)
DB_PATH = Path("air_quality.db")

def load_to_sql(df: pd.DataFrame, table_name="air_quality"):
    if df.empty:
        logger.warning("Empty dataframe, skipping DB load")
        return
    with sqlite3.connect(DB_PATH) as conn:
        df.to_sql(table_name, conn, if_exists="replace", index=False)
    logger.info(f"Loaded {len(df)} rows to {table_name}")

def save_csv(df: pd.DataFrame, path="outputs/air_quality_cleaned.csv"):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    logger.info(f"Saved CSV to {path}")