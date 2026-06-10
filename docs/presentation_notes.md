
---

# 📄 `docs/presentation_notes.md`

```md
# Presentation Notes – Risk Intelligence Platform

## Slide 1: Title

**Risk Intelligence Platform**
Automated Country Risk Scoring System

---

## Slide 2: Problem

- Manual compliance screening is slow
- Risk data is fragmented
- Difficult to scale globally

---

## Slide 3: Solution

We built an automated pipeline that:

- Ingests global financial indicators
- Applies compliance screening rules
- Generates risk scores
- Trains a machine learning model
- Produces explainable outputs

---

## Slide 4: Data Sources

- World Bank API (macro indicators)
- Sanctions lists (simulated)
- Governance indicators

---

## Slide 5: Pipeline Overview
Ingest → Validate → Clean → Screen → Feature Engineering
→ Model Training → Scoring → Reporting


---

## Slide 6: Feature Engineering

We generate risk signals such as:

- Economic risk
- Governance risk
- Corruption risk
- Regulatory risk
- Sanctions exposure

---

## Slide 7: Model

- Random Forest Classifier
- Predicts high-risk vs low-risk countries
- Outputs probability score

---

## Slide 8: Outputs

- Risk score per country
- Binary classification
- Feature importance
- Executive summary report

---

## Slide 9: Dashboard

Built with Streamlit:

- Total entities
- High-risk count
- Risk distribution
- Data preview

---

## Slide 10: Business Value

- Faster compliance decisions
- Scalable global screening
- Improved risk transparency
- Audit-friendly outputs

---

## Slide 11: Future Work

- Real-time data ingestion
- Advanced ML models
- Geospatial risk mapping
- Entity-level screening

---

## Slide 12: Closing

An end-to-end ML pipeline for automated, explainable risk intelligence.
