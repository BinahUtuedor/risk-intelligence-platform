"""
entity_screening.py

Purpose
-------
Perform sanctions screening
against countries.

Creates risk indicators
used by downstream models.

Output
------
data/processed/countries_screened.csv
"""

import pandas as pd

from config import (
    PROCESSED_DIR
)

SANCTIONED_COUNTRIES = [

    "Iran",

    "North Korea",

    "Russia",

    "Syria"

]

PEP_HIGH_RISK = [

    "Russia",

    "Belarus"

]

HIGH_RISK_JURISDICTIONS = [

    "Iran",

    "North Korea",

    "Russia",

    "Belarus",

    "Syria",

    "Afghanistan"

]


def screen_entities():

    df = pd.read_csv(
        PROCESSED_DIR /
        "countries_clean.csv"
    )

    # Sanctions screening

    df["sanction_risk"] = (

        df["country"]

        .isin(
            SANCTIONED_COUNTRIES
        )

        .astype(int)

    )

    # Politically exposed risk

    df["pep_risk"] = (

        df["country"]

        .isin(
            PEP_HIGH_RISK
        )

        .astype(int)

    )

    # High-risk jurisdiction

    df["high_risk_jurisdiction"] = (

        df["country"]

        .isin(
            HIGH_RISK_JURISDICTIONS
        )

        .astype(int)

    )

    output_file = (

        PROCESSED_DIR

        / "countries_screened.csv"

    )

    df.to_csv(
        output_file,
        index=False
    )

    print(
        f"Saved screened file to {output_file}"
    )


if __name__ == "__main__":

    screen_entities()