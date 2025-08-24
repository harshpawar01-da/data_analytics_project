import pandas as pd
from pathlib import Path

IN_PATH = Path("data/processed/mumbai_air_quality_clean.csv")
OUT_PATH = Path("data/processed/mumbai_air_quality_features.csv")

def categorize_pm25(x: float) -> str:
    if pd.isna(x): return "Unknown"
    if x <= 30: return "Good"
    if x <= 60: return "Satisfactory"
    if x <= 90: return "Moderate"
    if x <= 120: return "Poor"
    if x <= 250: return "Very Poor"
    return "Severe"

def main():
    df = pd.read_csv(IN_PATH, parse_dates=["date"])
    df = df.sort_values(["station", "date"])

    # Time features
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["dayofweek"] = df["date"].dt.dayofweek
    df["is_weekend"] = df["dayofweek"].isin([5,6]).astype(int)

    # Rolling features by station
    df = df.groupby("station", group_keys=False, observed=True).apply(
    lambda g: g.assign(
        pm25_roll7=g["pm25"].rolling(7, min_periods=1).mean(),
        pm25_roll30=g["pm25"].rolling(30, min_periods=7).mean()
    )
).reset_index(drop=True)

    # Category
    df["pm25_category"] = df["pm25"].apply(categorize_pm25)

    df.to_csv(OUT_PATH, index=False)
    print(f"[OK] Saved features to {OUT_PATH}")

if __name__ == "__main__":
    main()
