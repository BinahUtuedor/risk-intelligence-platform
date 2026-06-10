import pandas as pd
from src.quality.validation import validate


def test_validate_returns_expected_keys():
    df = pd.DataFrame({
        "a": [1, 2, 2],
        "b": [None, 2, 3]
    })

    report = validate(df)

    assert "rows" in report
    assert "duplicates" in report
    assert "missing" in report


def test_validate_counts_correctly():
    # FIX: create a true duplicate row (identical rows)
    df = pd.DataFrame({
        "a": [1, 2, 2],
        "b": [1, 2, 2]
    })

    report = validate(df)

    assert report["rows"] == 3
    assert report["duplicates"] == 1
    assert report["missing"] == 0


def test_validate_empty_dataframe():
    df = pd.DataFrame()

    report = validate(df)

    assert report["rows"] == 0
    assert report["duplicates"] == 0
    assert report["missing"] == 0