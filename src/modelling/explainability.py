"""
Model Explainability.

Produces:
- feature importance report
"""

import pandas as pd
import joblib

from config import MODEL_DIR, REPORT_DIR


def run_explainability():
    model = joblib.load(MODEL_DIR / "risk_model.pkl")

    feature_names = [
        "economic_risk",
        "tax_capacity_risk",
        "governance_risk",
        "corruption_risk",
        "regulatory_risk",
        "sanction_risk",
        "pep_risk",
        "high_risk_jurisdiction"
    ]

    importance = pd.DataFrame({
        "feature": feature_names,
        "importance": model.feature_importances_
    })

    output_file = REPORT_DIR / "feature_importance.csv"

    importance.to_csv(output_file, index=False)

    print(f"Saved feature importance to {output_file}")


if __name__ == "__main__":
    run_explainability()