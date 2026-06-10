# Risk Intelligence Platform

An end-to-end Risk Intelligence and Compliance Analytics platform that automates country-level risk assessment using public economic indicators, sanctions screening logic, machine learning, explainability, and executive reporting.

The project demonstrates practical applications of:

- Risk Analytics
- Compliance Monitoring
- AML / KYC Screening Concepts
- Data Engineering
- Machine Learning
- Explainable AI
- Dashboard Development

---

# Project Overview

Financial institutions, compliance teams, and risk analysts often need to assess exposure to:

- Economic instability
- Corruption risk
- Weak governance
- Regulatory weaknesses
- Sanctioned jurisdictions
- Politically Exposed Person (PEP) exposure

Manual assessment processes are difficult to scale and maintain.

This platform automates the process by:

1. Ingesting country-level indicators from the World Bank API
2. Performing data validation and cleansing
3. Applying sanctions and compliance screening rules
4. Engineering explainable risk features
5. Training a machine learning model
6. Scoring countries by risk level
7. Generating executive reports
8. Visualising outputs through a Streamlit dashboard

---

# Business Problem

Compliance and risk teams require a scalable way to identify high-risk countries and prioritise investigations.

Traditional approaches often rely on:

- Manual spreadsheets
- Static watchlists
- Fragmented data sources
- Subjective scoring methodologies

The Risk Intelligence Platform provides:

- Automated risk assessment
- Transparent scoring logic
- Explainable machine learning outputs
- Executive-ready reporting

---

# Solution Architecture

```text
World Bank API
       │
       ▼
┌─────────────────┐
│ Data Ingestion  │
└─────────────────┘
       │
       ▼
┌─────────────────┐
│ Data Validation │
└─────────────────┘
       │
       ▼
┌─────────────────┐
│ Data Cleaning   │
└─────────────────┘
       │
       ▼
┌─────────────────┐
│ Risk Screening  │
│ Sanctions / PEP │
└─────────────────┘
       │
       ▼
┌─────────────────┐
│ Feature         │
│ Engineering     │
└─────────────────┘
       │
       ▼
┌─────────────────┐
│ ML Modelling    │
└─────────────────┘
       │
       ▼
┌─────────────────┐
│ Explainability  │
└─────────────────┘
       │
       ▼
┌─────────────────┐
│ Reporting       │
└─────────────────┘
       │
       ▼
┌─────────────────┐
│ Dashboard       │
└─────────────────┘
```

---

# Project Structure

```text
risk-intelligence-platform/

├── data/
│   ├── raw/
│   ├── validated/
│   ├── processed/
│   └── reports/
│
├── dashboard/
│   └── dashboard.py
│
├── docs/
│
├── models/
│   └── risk_model.pkl
│
├── src/
│   ├── ingest/
│   ├── quality/
│   ├── screening/
│   ├── features/
│   ├── modelling/
│   └── reporting/
│
├── tests/
│
├── config.py
├── main.py
└── requirements.txt
```

---

# Data Sources

## World Bank API

The platform retrieves country-level indicators from the World Bank.

Indicators used:

| Indicator | Description |
|------------|------------|
| GDP | Current USD GDP |
| Tax Revenue | % of GDP |
| Control of Corruption | Governance indicator |
| Government Effectiveness | Governance indicator |
| Regulatory Quality | Governance indicator |

---

# Risk Screening Logic

The platform applies rule-based compliance checks.

## Sanction Risk

Countries identified on a sanctions watchlist receive:

```python
sanction_risk = 1
```

---

## PEP Risk

Countries associated with elevated politically exposed person risk receive:

```python
pep_risk = 1
```

---

## High-Risk Jurisdictions

Countries on a predefined high-risk list receive:

```python
high_risk_jurisdiction = 1
```

---

# Feature Engineering

The platform converts raw indicators into explainable binary risk signals.

Generated features:

| Feature | Description |
|----------|------------|
| economic_risk | GDP below median |
| tax_capacity_risk | Tax revenue below median |
| governance_risk | Weak government effectiveness |
| corruption_risk | High corruption exposure |
| regulatory_risk | Weak regulatory quality |

---

## Composite Risk Score

Risk signals are aggregated into a single score:

```text
risk_score =
economic_risk +
tax_capacity_risk +
governance_risk +
corruption_risk +
regulatory_risk +
sanction_risk +
pep_risk +
high_risk_jurisdiction
```

---

## Target Variable

```python
risk_flag = 1 if risk_score >= 3 else 0
```

---

# Machine Learning Model

## Algorithm

Random Forest Classifier

```python
RandomForestClassifier(
    n_estimators=200,
    random_state=42
)
```

---

## Features Used

```python
[
    "economic_risk",
    "tax_capacity_risk",
    "governance_risk",
    "corruption_risk",
    "regulatory_risk",
    "sanction_risk",
    "pep_risk",
    "high_risk_jurisdiction"
]
```

---

## Evaluation

Model evaluation includes:

- Accuracy
- Precision
- Recall
- F1 Score

Generated using:

```python
classification_report()
```

---

# Explainability

Feature importance is extracted from the trained model:

```python
model.feature_importances_
```

Output:

```text
data/reports/feature_importance.csv
```

This enables:

- Regulatory transparency
- Auditability
- Business interpretation

---

# Executive Reporting

The platform automatically generates:

## Scored Entities

```text
data/reports/scored_entities.csv
```

Contains:

- Risk score
- Predicted risk probability
- Risk classification

---

## Feature Importance Report

```text
data/reports/feature_importance.csv
```

---

## Executive Summary

```text
data/reports/executive_summary.csv
```

Includes:

- Total entities analysed
- High-risk entities
- Average risk score
- Top risk driver

---

# Dashboard

Built using Streamlit.

Launch:

```bash
streamlit run dashboard/dashboard.py
```

Dashboard includes:

- Total records
- High-risk count
- Risk score distribution
- Dataset explorer

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/risk-intelligence-platform.git

cd risk-intelligence-platform
```

---

## Create Virtual Environment

Windows:

```bash
python -m venv venv

venv\Scripts\activate
```

Mac/Linux:

```bash
python -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Pipeline

Execute the full workflow:

```bash
python main.py
```

Pipeline execution order:

1. Data Ingestion
2. Validation
3. Cleaning
4. Entity Screening
5. Feature Engineering
6. Model Training
7. Entity Scoring
8. Explainability
9. Executive Reporting

---

# Testing

Run all tests:

```bash
pytest
```

Run specific tests:

```bash
pytest tests/test_validation.py

pytest tests/test_features.py

pytest tests/test_modelling.py
```

---

# Example Outputs

Generated artifacts:

```text
data/raw/countries.csv

data/validated/validation_report.csv

data/processed/risk_dataset.csv

data/reports/scored_entities.csv

data/reports/feature_importance.csv

data/reports/executive_summary.csv

models/risk_model.pkl
```

---

# Skills Demonstrated

### Data Engineering

- Data ingestion pipelines
- Data validation
- Data cleaning
- Modular architecture

### Risk Analytics

- Compliance screening
- Sanctions logic
- Jurisdiction risk assessment

### Machine Learning

- Classification modelling
- Feature engineering
- Explainability

### Software Engineering

- Modular package structure
- Configuration management
- Automated pipeline orchestration
- Unit testing

### Dashboarding

- Streamlit applications
- Executive reporting

---

# Future Enhancements

- OpenSanctions API integration
- Real-time sanctions screening
- Country risk trend analysis
- Geospatial risk visualisation
- FastAPI scoring endpoint
- Docker deployment
- Cloud deployment (AWS / Azure)
- Airflow orchestration

---

# Author

Data Engineering | Risk Analytics | Machine Learning

This project was built as a portfolio demonstration of an end-to-end Risk Intelligence platform combining compliance analytics, data engineering, machine learning, and explainable AI.