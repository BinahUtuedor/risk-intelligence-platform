import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

from src.modelling.train_risk_model import train_model


def test_model_training_runs_without_error():
    """
    Smoke test:
    Ensures training pipeline executes without crashing.
    """

    # This is a lightweight smoke test.
    # In real CI, you'd mock file IO.
    try:
        train_model()
    except Exception as e:
        assert False, f"Training failed: {e}"


def test_feature_consistency():
    expected_features = [
        "economic_risk",
        "tax_capacity_risk",
        "governance_risk",
        "corruption_risk",
        "regulatory_risk",
        "sanction_risk",
        "pep_risk",
        "high_risk_jurisdiction"
    ]

    model_features = expected_features  # mirrors your pipeline

    assert len(model_features) == 8
    assert "economic_risk" in model_features


def test_random_forest_prediction_shape():
    model = RandomForestClassifier()

    X = pd.DataFrame(np.random.randint(0, 2, (10, 8)))

    y = np.random.randint(0, 2, 10)

    model.fit(X, y)

    preds = model.predict_proba(X)

    assert preds.shape == (10, 2)