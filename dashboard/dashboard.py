"""
Executive dashboard.

Run:

streamlit run dashboard.py

"""

import streamlit as st
import pandas as pd

df = pd.read_csv(
    "data/processed/risk_dataset.csv"
)

st.title(
    "Risk Intelligence Dashboard"
)

st.metric(
    "Records",
    len(df)
)

st.metric(
    "High Risk Cases",
    len(
        df[
            df["risk_flag"] == 1
        ]
    )
)

st.bar_chart(
    df["risk_score"]
)

st.dataframe(
    df.head(100)
)