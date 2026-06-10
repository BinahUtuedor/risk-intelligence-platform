"""
Download sanctions reference data.

This demonstrates:

- compliance analytics
- screening
- risk intelligence

"""

import pandas as pd

from config import RAW_DIR


def create_sample_watchlist():

    watchlist = pd.DataFrame(
        {
            "entity_name": [
                "Entity A",
                "Entity B",
                "Entity C"
            ],
            "sanctioned": [
                1,
                1,
                0
            ],
            "pep_flag": [
                1,
                0,
                0
            ]
        }
    )

    watchlist.to_csv(
        RAW_DIR /
        "sanctions.csv",
        index=False
    )


if __name__ == "__main__":
    create_sample_watchlist()