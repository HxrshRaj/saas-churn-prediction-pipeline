#  Predictive SaaS Churn Pipeline

> End-to-end ML system for predicting customer churn using XGBoost with real-time API and dashboard.

---

##  Problem

SaaS companies lose revenue due to:

*  Customer churn
*  Lack of predictive insights

This project predicts churn risk using **machine learning + real-time serving**.

---

##  Pipeline

Data → Preprocessing → Feature Engineering
          ↓
     Model Training (XGBoost)
          ↓
     Model Registry (versioned)
          ↓
     API (FastAPI)
          ↓
     Dashboard (Streamlit)

---

## ⚙️ Tech Stack

* Pandas (data processing)
* XGBoost (ML model)
* FastAPI (serving)
* Streamlit (visualization)

---

## 🔥 Key Features

###  Feature Engineering

* Engagement score
* Usage-based risk indicators

###  Model Versioning

* Reproducible experiments

###  Real-time API

* Low-latency predictions

###  Dashboard

* Visual churn insights

---

##  Impact

*  Improved churn prediction accuracy
* ⚡ Real-time decision-making capability
*  Actionable business insights

---

## 🧪 Example API

```bash
GET /predict?x=5.2
```

---

## ⚖️ Design Decisions

| Decision            | Why                      |
| ------------------- | ------------------------ |
| XGBoost             | Strong for tabular data  |
| FastAPI             | Lightweight + fast       |
| Streamlit           | Rapid visualization      |
| Feature engineering | Boosts model performance |

---

##  Future Improvements

* Real SaaS dataset integration
* Feature store (Feast)
* A/B testing models
* Online learning

---

##  Author

Harsh Raj
AI + Backend Systems | Data-Driven Engineering
