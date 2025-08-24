import pandas as pd
import numpy as np
from pathlib import Path

RAW_PATH = Path("data/raw/mumbai_air_quality.csv")
OUT_PATH = Path("data/processed/mumbai_air_quality_clean.csv")
OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

def main():
    if not RAW_PATH.exists():
        raise FileNotFoundError(f"Raw file not found: {RAW_PATH}")

    df = pd.read_csv(RAW_PATH)

    # Normalize column names
    df.columns = [c.strip().lower() for c in df.columns]

    # Require a date column
    if "date" not in df.columns:
        raise ValueError("Expected a 'date' column in the CSV.")
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])

    # Harmonize pollutant names
    df = df.rename(columns={"pm2_5": "pm25", "pm2.5": "pm25"})

    # Ensure expected columns exist (fill NaN if missing)
    expected = ["pm25", "pm10", "no2", "so2", "o3", "co", "aqi"]
    for col in expected:
        if col not in df.columns:
            df[col] = np.nan

    # Coerce numeric
    for col in expected:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Basic sanity filtering
    for col in ["pm25", "pm10", "no2", "so2", "o3", "co"]:
        df.loc[(df[col] < 0) | (df[col] > 2000), col] = np.nan

    # Station fallback
    if "station" not in df.columns:
        df["station"] = "Unknown"

    # Drop duplicates and sort
    df = df.drop_duplicates(subset=["date", "station"]).sort_values(["date", "station"])

    df.to_csv(OUT_PATH, index=False)
    print(f"[OK] Saved {len(df):,} rows to {OUT_PATH}")

if __name__ == "__main__":
    main()
