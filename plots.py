import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

FEAT_PATH = Path("data/processed/mumbai_air_quality_features.csv")
FIG_DIR = Path("reports/figures")
FIG_DIR.mkdir(parents=True, exist_ok=True)

def plot_pm25_trend():
    df = pd.read_csv(FEAT_PATH, parse_dates=["date"])
    city_daily = df.groupby("date", as_index=False)["pm25"].mean()
    plt.figure()
    plt.plot(city_daily["date"], city_daily["pm25"])
    plt.title("Mumbai PM2.5 – Daily Average (Citywide)")
    plt.xlabel("Date"); plt.ylabel("PM2.5 (µg/m³)")
    plt.tight_layout()
    out = FIG_DIR / "pm25_daily_trend.png"
    plt.savefig(out, dpi=160)
    print(f"Saved {out}")

def plot_category_distribution():
    df = pd.read_csv(FEAT_PATH, parse_dates=["date"])
    counts = df["pm25_category"].value_counts().sort_index()
    plt.figure()
    plt.bar(counts.index.astype(str), counts.values)
    plt.title("PM2.5 Category Distribution (All Stations)")
    plt.xlabel("Category"); plt.ylabel("Days")
    plt.xticks(rotation=30)
    plt.tight_layout()
    out = FIG_DIR / "pm25_category_distribution.png"
    plt.savefig(out, dpi=160)
    print(f"Saved {out}")

if __name__ == "__main__":
    plot_pm25_trend()
    plot_category_distribution()
