import logging
import pandas as pd
import requests
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()
logger = logging.getLogger(__name__)

# Your existing cleaned file
FALLBACK_PATH = Path(__file__).parent / "Smart_Air_quality_intelligence_cleaned.csv"

def fetch_air_quality(city="Hyderabad", parameter="pm25", limit=100):
    """
    1. Try OpenAQ API
    2. If fails, use your existing CSV as fallback
    """
    # --- 1. API TRY ---
    try:
        # OpenAQ latest API - no key needed for basic
        url = "https://api.openaq.org/v3/locations"
        params = {
            "city": city,
            "limit": 5,
            "order_by": "lastUpdated"
        }
        headers = {}
        api_key = os.getenv("OPENAQ_API_KEY")
        if api_key and api_key!= "test":
            headers["X-API-Key"] = api_key

        resp = requests.get(url, params=params, headers=headers, timeout=10)

        if resp.status_code == 200:
            data = resp.json()
            results = data.get("results", [])
            if results:
                # Convert to simple dataframe for pipeline
                rows = []
                for loc in results:
                    rows.append({
                        "city": city,
                        "location": loc.get("name"),
                        "parameter": parameter,
                        "value": loc.get("parameters", [{}])[0].get("lastValue", 50) if loc.get("parameters") else 50,
                        "unit": "µg/m³"
                    })
                logger.info(f"API success: {len(rows)} records")
                return pd.DataFrame(rows)
        logger.warning(f"API failed ({resp.status_code}), using fallback CSV")

    except Exception as e:
        logger.warning(f"API error: {e}, using fallback CSV")

    # --- 2. FALLBACK ---
    if FALLBACK_PATH.exists():
        logger.info(f"Using fallback: {FALLBACK_PATH.name}")
        df = pd.read_csv(FALLBACK_PATH)
        # Make sure 'value' column exists for your pipeline
        if 'value' not in df.columns:
            # try to find pm2.5 / pm25 column and rename
            for col in ['pm2.5', 'pm25', 'PM2.5', 'PM25', 'pm_2_5']:
                if col in df.columns:
                    df['value'] = df[col]
                    break
        return df
    else:
        logger.error("No API and no fallback CSV found")
        return pd.DataFrame()

if __name__ == "__main__":
    df = fetch_air_quality()
    print(df.head())