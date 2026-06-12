import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

pipeline = [
    "src.ingest.ingest_worldbank",
    "src.quality.validation",
    "src.quality.cleaning",
    "src.screening.entity_screening",
    "src.features.feature_engineering",
    "src.modelling.train_risk_model",
    "src.modelling.score_entities",
    "src.modelling.explainability",
    "src.reporting.reporting"
]

for step in pipeline:
    print(f"\nRunning {step}")

    result = subprocess.run(
        [sys.executable, "-m", step],
        cwd=str(BASE_DIR),   # must be string for Windows safety
        check=True
    )

print("\nPipeline Complete")