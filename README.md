# Predictive SaaS Churn Analytics Pipeline

## Motivation (Business Impact)

Churn is gradual behavioral decay, not a sudden event.

Missing a churn-risk customer (false negative) is more expensive than a false positive.

This system prioritizes:

* High recall
* Early detection
* Actionable insights

---

## System Architecture & Design Mechanics

### Design Approach

#### Feature Engineering First

Key signals:

* Usage decay trends
* Support friction (tickets, delays)
* Engagement drop

---

#### Model Choice: XGBoost

* Strong for tabular data
* Captures non-linear relationships
* Handles missing values

---

#### Recall Optimization

* Class weighting
* Threshold tuning

Goal: minimize false negatives

---

### Pipeline Flow

1. Data ingestion
2. Preprocessing
3. Feature engineering
4. Model training
5. API serving
6. Dashboard visualization

---

## Tech Stack

* Python
* pandas
* XGBoost
* Flask
* Streamlit

---

## Service Topology

```
Data Source
  ↓
ETL + Feature Engineering
  ↓
XGBoost Model
  ↓
Flask API
  ↓
Streamlit Dashboard
```

---

## Local Setup / Execution

### Install

```bash
pip install -r requirements.txt
```

### Train Model

```bash
python train.py
```

### Run API

```bash
python app.py
```

### Run Dashboard

```bash
streamlit run dashboard.py
```

---

## Future Scope / Known Limitations

### Limitations

* Batch processing only
* Limited feature coverage
* No automated retraining

### Future Work

* Real-time inference
* AutoML feature selection
* CRM integration
* SHAP explainability
* Feedback loop retraining

---

## Consultant Disclaimer

This project outlines system architecture and modeling strategy for churn prediction. Proprietary datasets, feature mappings, and business thresholds are excluded due to enterprise IP restrictions. Additional modeling details can be shared upon request.
