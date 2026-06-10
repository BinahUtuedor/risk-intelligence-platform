"""
ingest_worldbank.py

Purpose
-------
Download multiple World Bank indicators
and create a country-level risk dataset.

Indicators
----------
NY.GDP.MKTP.CD
    GDP (Current USD)

GC.TAX.TOTL.GD.ZS
    Tax Revenue (% GDP)

CC.EST
    Control of Corruption

GE.EST
    Government Effectiveness

RQ.EST
    Regulatory Quality

Output
------
data/raw/countries.csv

Author
------
Risk Intelligence Platform
"""

import requests
import pandas as pd

from config import RAW_DIR

INDICATORS = {
    "NY.GDP.MKTP.CD": "gdp",
    "GC.TAX.TOTL.GD.ZS": "tax_revenue_pct",
    "CC.EST": "control_of_corruption",
    "GE.EST": "government_effectiveness",
    "RQ.EST": "regulatory_quality"
}


def download_indicator(indicator_code):
    """
    Download a World Bank indicator.
    """

    url = (
        "https://api.worldbank.org/v2/"
        f"country/all/indicator/{indicator_code}"
        "?format=json&per_page=20000"
    )

    response = requests.get(
        url,
        timeout=60
    )

    response.raise_for_status()

    return response.json()


def build_country_dataset():
    """
    Build unified dataset.
    """

    indicator_frames = []

    for code, name in INDICATORS.items():

        print(f"Downloading {name}")

        data = download_indicator(code)

        rows = []

        if len(data) < 2:
            continue

        for record in data[1]:

            rows.append(
                {
                    "country": record["country"]["value"],
                    "country_code": record["countryiso3code"],
                    "year": record["date"],
                    name: record["value"]
                }
            )

        df = pd.DataFrame(rows)

        indicator_frames.append(df)

    merged = indicator_frames[0]

    for df in indicator_frames[1:]:

        merged = merged.merge(
            df,
            on=[
                "country",
                "country_code",
                "year"
            ],
            how="outer"
        )

    # Use latest available year only

    merged["year"] = pd.to_numeric(
        merged["year"],
        errors="coerce"
    )

    merged = merged.sort_values(
        "year",
        ascending=False
    )

    merged = merged.groupby(
        "country_code",
        as_index=False
    ).first()

    output_file = (
        RAW_DIR /
        "countries.csv"
    )

    merged.to_csv(
        output_file,
        index=False
    )

    print(
        f"Saved {len(merged)} countries "
        f"to {output_file}"
    )


if __name__ == "__main__":

    build_country_dataset()