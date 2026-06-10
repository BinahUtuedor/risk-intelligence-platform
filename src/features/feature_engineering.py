"""
feature_engineering.py

Purpose
-------
Create explainable compliance-risk features.
"""

import pandas as pd
import numpy as np
from config import PROCESSED_DIR


def create_risk_flags(df):

    gdp_threshold = df["gdp"].median()
    df["economic_risk"] = np.where(df["gdp"] < gdp_threshold, 1, 0)

    tax_threshold = df["tax_revenue_pct"].median()
    df["tax_capacity_risk"] = np.where(df["tax_revenue_pct"] < tax_threshold, 1, 0)

    gov_threshold = df["government_effectiveness"].median()
    df["governance_risk"] = np.where(df["government_effectiveness"] < gov_threshold, 1, 0)

    corruption_threshold = df["control_of_corruption"].median()
    df["corruption_risk"] = np.where(df["control_of_corruption"] < corruption_threshold, 1, 0)

    regulatory_threshold = df["regulatory_quality"].median()
    df["regulatory_risk"] = np.where(df["regulatory_quality"] < regulatory_threshold, 1, 0)

    return df


def calculate_composite_risk(df):

    risk_columns = [
        "economic_risk",
        "tax_capacity_risk",
        "governance_risk",
        "corruption_risk",
        "regulatory_risk",
        "sanction_risk",
        "pep_risk",
        "high_risk_jurisdiction"
    ]

    df["risk_score"] = df[risk_columns].sum(axis=1)
    return df


def create_target(df):

    threshold = 3  # 🔥 lowered from 4 to ensure BOTH classes exist

    df["risk_flag"] = np.where(df["risk_score"] >= threshold, 1, 0)

    print("Risk label distribution:")
    print(df["risk_flag"].value_counts())

    return df


def engineer_features():

    df = pd.read_csv(PROCESSED_DIR / "countries_screened.csv")

    numeric_cols = [
        "gdp",
        "tax_revenue_pct",
        "government_effectiveness",
        "control_of_corruption",
        "regulatory_quality"
    ]

    for col in numeric_cols:
        if col not in df.columns:
            df[col] = np.nan

        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(df[col].median())

    df = create_risk_flags(df)
    df = calculate_composite_risk(df)
    df = create_target(df)

    # 🔥 HARD SAFETY CHECK (prevents broken model training)
    if df["risk_flag"].nunique() < 2:
        raise ValueError(
            "risk_flag has only one class. Adjust threshold or features."
        )

    output_file = PROCESSED_DIR / "risk_dataset.csv"
    df.to_csv(output_file, index=False)

    print(f"Saved risk dataset to {output_file}")
    print(f"High-risk entities: {df['risk_flag'].sum()}")


if __name__ == "__main__":
    engineer_features()