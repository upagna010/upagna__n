import pandas as pd
import requests
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def fetch_air_quality(city="Hyderabad", parameter="pm25", limit=100) -> pd.DataFrame:
    # 1. Try new OpenAQ v3 (needs no key for limited)
    try:
        url = f"https://api.openaq.org/v3/locations"
        params = {"city": city, "limit": 10}
        resp = requests.get(url, params=params, timeout=15)
        if resp.status_code == 200:
            logger.info("Fetched from OpenAQ v3")
            # v3 format different, convert to simple rows
            data = resp.json().get("results", [])
            rows = []
            for r in data[:limit]:
                rows.append({
                    "city": city,
                    "location": r.get("name"),
                    "parameter": parameter,
                    "value": r.get("parameters", [{}])[0].get("lastValue", 0) if r.get("parameters") else 0,
                    "unit": "µg/m³",
                    "lastUpdated": r.get("datetimeLast", {}).get("utc", "")
                })
            if rows:
                return pd.DataFrame(rows)
    except Exception as e:
        logger.warning(f"OpenAQ v3 failed: {e}")

    # 2. FALLBACK - Production pattern: use your existing cleaned CSV
    fallback_path = Path("final_air_quality.csv")
    if fallback_path.exists():
        logger.warning(f"API Gone (410), using fallback {fallback_path}")
        df = pd.read_csv(fallback_path)
        # Normalize column names to our pipeline format
        if "value" not in df.columns and "pm25" in df.columns:
            df = df.rename(columns={"pm25": "value"})
        return df.head(limit)

    logger.error("No API and no fallback CSV found")
    return pd.DataFrame()