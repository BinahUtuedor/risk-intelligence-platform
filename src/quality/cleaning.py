"""
cleaning.py

Purpose
-------
Apply cleaning rules after validation.
"""

import pandas as pd
from config import RAW_DIR, PROCESSED_DIR


def clean_countries():
    df = pd.read_csv(RAW_DIR / "countries.csv")

    initial_rows = len(df)

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove blank countries
    df = df[df["country"].notna()]

    # Standardise country names
    df["country"] = df["country"].astype(str).str.strip()

    # Expected numeric columns
    numeric_cols = [
        "gdp",
        "tax_revenue_pct",
        "control_of_corruption",
        "government_effectiveness",
        "regulatory_quality"
    ]

    # Ensure numeric conversion safely
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # only use columns that actually exist
    existing_numeric_cols = [c for c in numeric_cols if c in df.columns]

    if existing_numeric_cols:
        df = df.dropna(subset=existing_numeric_cols, how="all")

    final_rows = len(df)

    print(f"Rows removed: {initial_rows - final_rows}")

    output_file = PROCESSED_DIR / "countries_clean.csv"
    df.to_csv(output_file, index=False)

    print(f"Saved cleaned data to {output_file}")


if __name__ == "__main__":
    clean_countries()