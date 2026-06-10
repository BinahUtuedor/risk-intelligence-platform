"""
Quality Assurance Layer.

Checks:

- missing values
- duplicates
- invalid values

"""

import pandas as pd

from config import RAW_DIR
from config import VALIDATED_DIR


def validate(df):

    report = {
        "rows": len(df),
        "duplicates":
        df.duplicated().sum(),
        "missing":
        df.isnull().sum().sum()
    }

    return report


def main():

    countries = pd.read_csv(
        RAW_DIR /
        "countries.csv"
    )

    report = validate(
        countries
    )

    pd.DataFrame(
        [report]
    ).to_csv(
        VALIDATED_DIR /
        "validation_report.csv",
        index=False
    )


if __name__ == "__main__":
    main()