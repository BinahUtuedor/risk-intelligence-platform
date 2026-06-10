import pandas as pd
from src.features.feature_engineering import (
    create_risk_flags,
    calculate_composite_risk,
    create_target
)


def sample_df():
    return pd.DataFrame({
        "gdp": [100, 200, 300],
        "tax_revenue_pct": [10, 20, 30],
        "government_effectiveness": [0.2, 0.5, 0.9],
        "control_of_corruption": [0.1, 0.4, 0.8],
        "regulatory_quality": [0.3, 0.6, 0.9],
        "sanction_risk": [0, 1, 0],
        "pep_risk": [0, 0, 1],
        "high_risk_jurisdiction": [1, 0, 0]
    })


def test_create_risk_flags_adds_columns():
    df = sample_df()

    df = create_risk_flags(df)

    expected_cols = [
        "economic_risk",
        "tax_capacity_risk",
        "governance_risk",
        "corruption_risk",
        "regulatory_risk"
    ]

    for col in expected_cols:
        assert col in df.columns


def test_calculate_composite_risk():
    df = sample_df()
    df = create_risk_flags(df)
    df = calculate_composite_risk(df)

    assert "risk_score" in df.columns
    assert df["risk_score"].dtype != "O"  # not object


def test_create_target_binary_output():
    df = sample_df()
    df = create_risk_flags(df)
    df = calculate_composite_risk(df)
    df = create_target(df)

    assert "risk_flag" in df.columns
    assert set(df["risk_flag"].unique()).issubset({0, 1})