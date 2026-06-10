"""
Global configuration.

Stores:

- paths
- model settings
- API endpoints

"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

RAW_DIR = DATA_DIR / "raw"

VALIDATED_DIR = DATA_DIR / "validated"

PROCESSED_DIR = DATA_DIR / "processed"

REPORT_DIR = DATA_DIR / "reports"

MODEL_DIR = BASE_DIR / "models"

RANDOM_STATE = 42

TEST_SIZE = 0.20

WORLD_BANK_URL = (
    "https://api.worldbank.org/v2"
)

OPENSANCTIONS_URL = (
    "https://www.opensanctions.org"
)