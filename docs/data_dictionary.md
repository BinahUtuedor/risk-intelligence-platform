
---

# 📄 `docs/data_dictionary.md`

```md
# Data Dictionary – Risk Intelligence Platform

## Overview

This document describes the structure of datasets used in the Risk Intelligence Platform.

---

# 1. Raw Dataset (`countries.csv`)

## Source

World Bank API

## Fields

| Column | Description |
|--------|------------|
| country | Country name |
| country_code | ISO3 country code |
| year | Data year |
| gdp | GDP (current USD) |
| tax_revenue_pct | Tax revenue (% of GDP) |
| control_of_corruption | Governance indicator |
| government_effectiveness | Government efficiency score |
| regulatory_quality | Regulatory quality score |

---

# 2. Clean Dataset (`countries_clean.csv`)

## Processed Features

Same as raw dataset with:

- Duplicates removed
- Missing values handled
- Numeric type enforcement

---

# 3. Screened Dataset (`countries_screened.csv`)

## Added Fields

| Column | Description |
|--------|------------|
| sanction_risk | 1 if country is in sanctions list |
| pep_risk | Politically exposed country flag |
| high_risk_jurisdiction | High-risk jurisdiction indicator |

---

# 4. Feature Engineered Dataset (`risk_dataset.csv`)

## Risk Flags

| Feature | Description |
|--------|------------|
| economic_risk | Low GDP relative to median |
| tax_capacity_risk | Low tax revenue capacity |
| governance_risk | Weak government effectiveness |
| corruption_risk | High corruption levels |
| regulatory_risk | Weak regulatory quality |

---

## Composite Features

| Feature | Description |
|--------|------------|
| risk_score | Sum of all risk indicators |
| risk_flag | Binary classification (0/1) |

---

# 5. Model Output Dataset (`scored_entities.csv`)

| Column | Description |
|--------|------------|
| predicted_risk_score | Model probability score |
| risk_score | Rule-based score |
| risk_flag | True label |

---

# 6. Feature Importance (`feature_importance.csv`)

| Column | Description |
|--------|------------|
| feature | Model input feature |
| importance | Random Forest importance score |

---

# Data Flow Summary
```text
World Bank API
↓
countries.csv
↓
cleaning
↓
countries_clean.csv
↓
screening
↓
countries_screened.csv
↓
feature engineering
↓
risk_dataset.csv
↓
model training + scoring
↓
reports/
```

