# Risk Intelligence Platform

### From Public Indicators to Explainable Country Risk Decisions — An End-to-End Risk Analytics and Compliance Intelligence Platform

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-machine--learning-orange)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-dashboard-red)](https://streamlit.io/)
[![World%20Bank](https://img.shields.io/badge/world_bank-public_data-green)](https://data.worldbank.org/)
[![Explainable%20AI](https://img.shields.io/badge/XAI-explainability-purple)](#)

## 📌 Overview

The Risk Intelligence Platform is an end-to-end compliance analytics solution designed to automate country-level risk assessment using publicly available economic indicators, rule-based screening logic, machine learning, explainability techniques, and executive reporting.

The platform simulates how financial institutions, compliance teams, correspondent banks, and risk analysts assess exposure to high-risk jurisdictions in a scalable and transparent manner.

It demonstrates the practical application of modern analytical techniques across multiple disciplines.

### Core Capabilities

* ✅ Country-level risk intelligence
* ✅ Automated data ingestion from public sources
* ✅ Data quality validation and cleansing
* ✅ Sanctions and compliance screening logic
* ✅ Explainable feature engineering
* ✅ Machine learning–driven risk classification
* ✅ Executive reporting and analytics outputs
* ✅ Interactive dashboard visualisation
* ✅ Modular and extensible architecture

---

## 🎯 Business Problem

Financial institutions and regulated organisations routinely assess jurisdictional exposure arising from:

* Economic instability
* Corruption risk
* Weak governance frameworks
* Regulatory deficiencies
* Sanctioned countries
* Politically Exposed Person (PEP) concerns
* High-risk jurisdictions requiring enhanced due diligence

Traditional approaches often rely on:

* Manual spreadsheets
* Static watchlists
* Subjective assessments
* Fragmented data sources
* Limited transparency
* Difficult-to-maintain scoring methodologies

These approaches become increasingly difficult to scale as regulatory expectations evolve.

---

## 💡 Solution

The Risk Intelligence Platform automates the risk assessment lifecycle by:

1. Retrieving country indicators from the World Bank API.
2. Validating and cleansing incoming datasets.
3. Applying sanctions and compliance screening logic.
4. Engineering explainable risk signals.
5. Training a machine learning classification model.
6. Generating country-level risk scores.
7. Producing executive reporting outputs.
8. Visualising findings through an interactive dashboard.

The result is a transparent, auditable, and repeatable risk intelligence process.

---

## 🗺️ Architecture Overview

The platform follows a modern layered analytics architecture.

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
                     │ Executive       │
                     │ Reporting       │
                     └─────────────────┘
                                │
                                ▼
                     ┌─────────────────┐
                     │ Dashboard       │
                     │ Visualisation   │
                     └─────────────────┘
```

---

## 🔄 Risk Assessment Workflow

The end-to-end workflow consists of nine stages:

1. Data ingestion from the World Bank API.
2. Dataset validation and profiling.
3. Data cleansing and standardisation.
4. Compliance screening and enrichment.
5. Feature engineering.
6. Machine learning model training.
7. Country-level risk scoring.
8. Explainability analysis.
9. Executive reporting and dashboard publication.

---

## 🛠️ Technology Stack

| Tool           | Purpose                         | Version | Installation Method |
| -------------- | ------------------------------- | ------- | ------------------- |
| Python         | Core programming language       | 3.10+   | Native              |
| Pandas         | Data manipulation and cleansing | Latest  | pip                 |
| NumPy          | Numerical computation           | Latest  | pip                 |
| Requests       | API integration                 | Latest  | pip                 |
| World Bank API | Country indicator source        | Latest  | Public API          |
| Scikit-Learn   | Machine learning                | Latest  | pip                 |
| Joblib         | Model persistence               | Latest  | pip                 |
| Streamlit      | Dashboard development           | Latest  | pip                 |
| Matplotlib     | Visualisation                   | Latest  | pip                 |
| Pytest         | Unit testing                    | Latest  | pip                 |

---

## 📁 Project Structure

```text
risk-intelligence-platform/
│
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
│   ├── data_dictionary.md
│   ├── data_lineage.md
│   └── architecture.md
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
├── requirements.txt
└── README.md
```

---

## 🌍 Data Sources

### World Bank API

The platform retrieves publicly available country-level indicators from the World Bank.

### Indicators Used

| Indicator                | Description                        |
| ------------------------ | ---------------------------------- |
| GDP                      | Current USD GDP                    |
| Tax Revenue              | Tax revenue as a percentage of GDP |
| Control of Corruption    | Governance effectiveness indicator |
| Government Effectiveness | Public sector quality indicator    |
| Regulatory Quality       | Regulatory effectiveness indicator |

---

## 🔍 Compliance Screening Logic

The platform applies deterministic screening rules commonly used within compliance environments.

### Sanctions Risk

Countries appearing on sanctions watchlists receive:

```python
sanction_risk = 1
```

---

### Politically Exposed Person (PEP) Risk

Countries associated with elevated PEP exposure receive:

```python
pep_risk = 1
```

---

### High-Risk Jurisdictions

Countries identified as requiring enhanced due diligence receive:

```python
high_risk_jurisdiction = 1
```

---

## ⚙️ Feature Engineering

Raw indicators are transformed into explainable binary signals.

### Engineered Features

| Feature                | Description                       |
| ---------------------- | --------------------------------- |
| economic_risk          | GDP below median                  |
| tax_capacity_risk      | Tax revenue below median          |
| governance_risk        | Weak government effectiveness     |
| corruption_risk        | Elevated corruption exposure      |
| regulatory_risk        | Weak regulatory quality           |
| sanction_risk          | Country appears on sanctions list |
| pep_risk               | Elevated PEP exposure             |
| high_risk_jurisdiction | Enhanced due diligence required   |

---

## 📊 Composite Risk Score

Risk signals are aggregated into a transparent score.

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

## 🎯 Target Variable

Countries are classified using the following rule:

```python
risk_flag = 1 if risk_score >= 3 else 0
```

This allows the model to learn patterns associated with elevated risk.

---

## 🤖 Machine Learning Model

### Algorithm

Random Forest Classifier

```python
RandomForestClassifier(
    n_estimators=200,
    random_state=42
)
```

---

### Features Used

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

## 📈 Model Evaluation

The model is evaluated using industry-standard metrics.

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score

Generated using:

```python
classification_report()
```

---

## 🔎 Explainability

Feature importance is extracted from the trained model.

```python
model.feature_importances_
```

Generated output:

```text
data/reports/feature_importance.csv
```

Explainability supports:

* Regulatory transparency
* Auditability
* Governance requirements
* Business interpretation
* Stakeholder trust

---

## 📑 Executive Reporting

The platform automatically produces executive-ready outputs.

### Scored Entities

```text
data/reports/scored_entities.csv
```

Contains:

* Country name
* Composite risk score
* Predicted probability
* Risk classification

---

### Feature Importance Report

```text
data/reports/feature_importance.csv
```

Contains:

* Ranked feature importance
* Relative contribution analysis

---

### Executive Summary

```text
data/reports/executive_summary.csv
```

Includes:

* Total countries analysed
* High-risk countries identified
* Average risk score
* Top contributing risk driver

---

## 📊 Dashboard

Built using Streamlit.

Launch:

```bash
streamlit run dashboard/dashboard.py
```

### Dashboard Features

* Total countries analysed
* High-risk country count
* Risk score distribution
* Country explorer
* Feature importance visualisation
* Executive summary metrics

---

## 🚀 Quick Start

### Prerequisites

Ensure the following are installed:

* Python 3.10+
* Git
* Internet connectivity for API access

---

### Clone Repository

```bash
git clone https://github.com/yourusername/risk-intelligence-platform.git

cd risk-intelligence-platform
```

---

### Create Virtual Environment

Windows:

```bash
python -m venv venv

venv\Scripts\activate
```

Linux/Mac:

```bash
python -m venv venv

source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Pipeline

Execute the complete workflow:

```bash
python main.py
```

Pipeline execution order:

1. Data ingestion
2. Validation
3. Cleaning
4. Compliance screening
5. Feature engineering
6. Model training
7. Country scoring
8. Explainability analysis
9. Executive reporting

---

## 🧪 Testing

Run all tests:

```bash
pytest
```

Run specific test suites:

```bash
pytest tests/test_validation.py

pytest tests/test_features.py

pytest tests/test_modelling.py
```

---

## 📂 Generated Outputs

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

## 📈 Performance Characteristics

| Component           | Typical Performance   |
| ------------------- | --------------------- |
| API Ingestion       | ~150 countries/minute |
| Validation          | ~500 records/second   |
| Feature Engineering | ~2,000 records/second |
| Model Training      | <5 seconds            |
| Risk Scoring        | ~5,000 records/second |
| Dashboard Refresh   | Near real-time        |

---

## 🔐 Governance & Security Considerations

* Public data sources eliminate exposure to customer information.
* Screening logic is fully transparent and explainable.
* Model outputs are reproducible.
* Executive reports support audit requirements.
* Explainability enhances regulatory confidence.
* Configuration settings are isolated from business logic.

---

## 🧠 Skills Demonstrated

### Risk Analytics

* Jurisdiction risk assessment
* Compliance screening
* PEP risk analysis
* Sanctions logic implementation

### Data Engineering

* API ingestion pipelines
* Data validation frameworks
* Data cleansing workflows
* Modular architecture design

### Machine Learning

* Classification modelling
* Feature engineering
* Explainable AI
* Model evaluation

### Software Engineering

* Configuration management
* Modular package design
* Automated workflows
* Unit testing

### Dashboarding

* Streamlit applications
* Executive reporting
* Interactive analytics

---

## 🚀 Future Enhancements

Potential extensions include:

* OpenSanctions API integration
* Real-time sanctions monitoring
* Country risk trend analysis
* Geospatial risk visualisation
* SHAP explainability dashboards
* FastAPI scoring endpoints
* Docker containerisation
* AWS or Azure deployment
* Apache Airflow orchestration
* CI/CD pipelines using GitHub Actions

---

## 📚 Resources

The following resources were used to inform the design and implementation of this platform:

* **World Bank Open Data** – Public economic and governance indicators used for country-level risk assessment.
  https://data.worldbank.org/

* **World Bank API Documentation** – Reference documentation for accessing World Bank indicators programmatically.
  https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation

* **Scikit-Learn Documentation** – Machine learning algorithms, model evaluation, and feature importance techniques.
  https://scikit-learn.org/stable/documentation.html

* **Pandas Documentation** – Data manipulation, validation, and transformation workflows.
  https://pandas.pydata.org/docs/

* **NumPy Documentation** – Numerical computing and array operations.
  https://numpy.org/doc/

* **Streamlit Documentation** – Building interactive dashboards and data applications.
  https://docs.streamlit.io/

* **Pytest Documentation** – Unit testing framework used to validate pipeline components.
  https://docs.pytest.org/

* **Requests Documentation** – HTTP client library used for API integration.
  https://requests.readthedocs.io/

* **Joblib Documentation** – Model serialisation and persistence for trained machine learning models.
  https://joblib.readthedocs.io/

* **OECD Recommendation on Artificial Intelligence** – Guidance on trustworthy and transparent AI practices relevant to explainability and governance.
  https://oecd.ai/en/ai-principles

* **Financial Action Task Force (FATF)** – International standards and guidance on AML/CFT risk-based approaches and high-risk jurisdictions.
  https://www.fatf-gafi.org/

* **Basel Committee on Banking Supervision** – Principles for sound risk management and supervisory expectations.
  https://www.bis.org/bcbs/

* **Office of Foreign Assets Control (OFAC)** – U.S. sanctions programmes and sanctions-related guidance.
  https://ofac.treasury.gov/

* **United Nations Security Council Sanctions Lists** – Reference source for international sanctions information.
  https://www.un.org/securitycouncil/sanctions/information

* **OpenSanctions** – Open-source sanctions and politically exposed persons (PEP) datasets for future platform enhancements.
  https://www.opensanctions.org/


---

## 📄 License

MIT License.

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a pull request.

---

## 👤 Author

**Binah Utuedor**

This project was developed as a portfolio demonstration of how modern risk intelligence platforms combine compliance analytics, data engineering, machine learning, and explainable AI to support transparent and scalable jurisdiction risk assessment.

---

## 🙏 Acknowledgements

Special thanks to:

* The World Bank Open Data initiative
* The Scikit-Learn community
* Streamlit contributors
* Open-source maintainers advancing responsible AI and compliance analytics

---

## 📞 Support

For issues and enhancements:

* Review the documentation.
* Check test outputs and generated reports.
* Open an issue in the repository.
* Submit enhancement requests through GitHub.
