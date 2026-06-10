"""
reporting.py

Purpose
-------
Generate executive-level reporting outputs
from the risk scoring pipeline.

Inputs
------
data/reports/scored_entities.csv
data/reports/feature_importance.csv

Outputs
-------
data/reports/executive_summary.csv

This report provides:
- Total entities analysed
- Number of high-risk entities
- Average risk score
- Most important model driver
"""

from pathlib import Path
import pandas as pd

from config import REPORT_DIR


def create_executive_summary():
    """
    Create a high-level summary report
    for business stakeholders.
    """

    # Define expected input files

    scored_file = REPORT_DIR / "scored_entities.csv"
    importance_file = REPORT_DIR / "feature_importance.csv"

    # Validate required files exist

    if not scored_file.exists():
        raise FileNotFoundError(
            f"Missing file: {scored_file}"
        )

    if not importance_file.exists():
        raise FileNotFoundError(
            f"Missing file: {importance_file}"
        )

    # Load model outputs

    scored = pd.read_csv(
        scored_file
    )

    importance = pd.read_csv(
        importance_file
    )

    # Identify the most influential feature
    # according to the trained model

    top_risk_driver = (

        importance

        .sort_values(
            "importance",
            ascending=False
        )

        .iloc[0]["feature"]

    )

    # Build executive summary metrics

    summary = pd.DataFrame(
        [{
            "total_entities":
                len(scored),

            "high_risk_entities":
                (
                    scored["risk_flag"] == 1
                ).sum(),

            "average_risk_score":
                round(
                    scored["risk_score"].mean(),
                    2
                ),

            "top_risk_driver":
                top_risk_driver
        }]
    )

    # Save report for dashboarding
    # and stakeholder consumption

    output_file = (
        REPORT_DIR /
        "executive_summary.csv"
    )

    summary.to_csv(
        output_file,
        index=False
    )

    print(
        f"Saved executive summary to "
        f"{output_file}"
    )


if __name__ == "__main__":

    create_executive_summary()