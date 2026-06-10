"""
train_risk_model.py

Purpose
-------
Train risk classification model.

Target
------
risk_flag

Output
------
models/risk_model.pkl
"""

import joblib
import pandas as pd

from sklearn.model_selection import (
    train_test_split
)

from sklearn.ensemble import (
    RandomForestClassifier
)

from sklearn.metrics import (
    accuracy_score,
    classification_report
)

from config import (
    MODEL_DIR,
    PROCESSED_DIR,
    TEST_SIZE,
    RANDOM_STATE
)


def train_model():

    df = pd.read_csv(
        PROCESSED_DIR /
        "risk_dataset.csv"
    )

    features = [

    "economic_risk",

    "tax_capacity_risk",

    "governance_risk",

    "corruption_risk",

    "regulatory_risk",

    "sanction_risk",

    "pep_risk",

    "high_risk_jurisdiction"

]

    X = df[features]

    y = df["risk_flag"]

    X_train, X_test, y_train, y_test = (

        train_test_split(

            X,

            y,

            test_size=TEST_SIZE,

            random_state=RANDOM_STATE

        )

    )

    model = RandomForestClassifier(

        n_estimators=200,

        random_state=RANDOM_STATE

    )

    model.fit(
        X_train,
        y_train
    )

    preds = model.predict(
        X_test
    )

    print(
        classification_report(
            y_test,
            preds
        )
    )

    print(
        "Accuracy:",
        accuracy_score(
            y_test,
            preds
        )
    )

    joblib.dump(

        model,

        MODEL_DIR /
        "risk_model.pkl"

    )


if __name__ == "__main__":

    train_model()