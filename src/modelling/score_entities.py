"""
score_entities.py

Purpose
-------
Generate investigation priority scores.

Output
------
data/reports/scored_entities.csv
"""

import joblib
import pandas as pd

from config import MODEL_DIR, PROCESSED_DIR, REPORT_DIR


def score():
    model = joblib.load(MODEL_DIR / "risk_model.pkl")

    df = pd.read_csv(PROCESSED_DIR / "risk_dataset.csv")

    # FIXED feature alignment (must match training)
    features = [
        "economic_risk",
        "tax_capacity_risk",
        "governance_risk",
        "corruption_risk",
        "regulatory_risk",
        "sanction_risk",
        "pep_risk",
        "high_risk_jurisdiction"
    ]

    df["predicted_risk_score"] = model.predict_proba(df[features])[:, 1]

    df = df.sort_values("predicted_risk_score", ascending=False)

    output_file = REPORT_DIR / "scored_entities.csv"

    df.to_csv(output_file, index=False)

    print(f"Saved {output_file}")


if __name__ == "__main__":
    score()