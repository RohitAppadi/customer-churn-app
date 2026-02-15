# 📌 Customer Churn Prediction System  
### End-to-End Machine Learning Deployment with Business Intelligence Integration

---

## 🚀 Overview

This project implements a complete **customer churn prediction system** using machine learning, cloud deployment, and business intelligence visualization.

The system predicts customer churn probability, calculates revenue exposure, and enables executive-level insights through Power BI dashboards.

It is designed as a **production-ready ML inference service**, not just a notebook experiment.

---

## 🎯 Business Objective

Telecom companies lose significant revenue due to customer churn.

This system answers:

- Which customers are likely to churn?
- How much revenue is at risk?
- What behavioral factors drive churn?
- How accurate is the model?

The output supports retention strategy planning and revenue protection decisions.

---

## 🧠 Machine Learning Pipeline

### Model Used
- Logistic Regression (with feature scaling)
- Stratified train-test split
- Threshold tuning using Precision-Recall optimization

### Data Processing
- Leakage column removal
- High-cardinality feature handling
- One-hot encoding
- Feature alignment using saved column schema
- StandardScaler transformation

### Performance (Test Set)
- **Accuracy:** ~80%
- **Recall (Churn):** ~66%
- **Precision (Churn):** ~61%
- Balanced F1-score

The decision threshold was tuned to improve churn detection without severely reducing overall accuracy.

---

## ☁️ Deployment Architecture
1. User Upload CSV
      ↓
2. Streamlit App (Replit Cloud)
      ↓
3. Model + Scaler + Feature Schema Loaded
      ↓
4. Predictions Generated
      ↓
5. Enriched CSV Output
      ↓
6. Power BI Dashboard

The model is deployed as a live cloud inference service using Streamlit on Replit.

---

## 🖥 Live Application

The deployed app allows:

- Uploading the original IBM telecom dataset
- Generating churn predictions
- Calculating revenue at risk
- Viewing KPI summary
- Downloading enriched prediction dataset

This simulates a real-world batch scoring system.

---

## 📊 Power BI Dashboard

The dashboard provides:

### Executive KPIs
- Total Customers
- High Risk Customers
- Revenue at Risk
- % Revenue at Risk

### Risk Distribution
- Predicted churn segmentation
- Revenue exposure by churn group

### Model Performance
- Accuracy
- Precision
- Recall
- Confusion matrix visualization

The BI layer translates ML output into actionable business insights.

---

## 🛠 Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib
- Power BI
- GitHub
- Replit (Cloud Hosting)

---

## 📂 Repository Structure
customer-churn-predictor/
│
├── app.py
├── requirements.txt
├── models/
│ ├── churn_model.pkl
│ ├── scaler.pkl
│ └── feature_columns.pkl

---

## 🔍 Key Features

- Production-ready model artifact saving
- Cloud deployment
- Robust feature alignment
- Scalable batch prediction system
- Business KPI integration
- End-to-end ML to BI workflow

---

## 📈 Business Impact

Using churn probability and revenue calculation:

- High-risk customers are identified
- Monthly revenue exposure is quantified
- Retention teams can prioritize intervention
- Decision-making becomes data-driven

This project bridges machine learning with actionable business intelligence.

---

## 📌 Future Improvements

- Automated Power BI web connection
- Model versioning
- Threshold simulation interface
- API-based inference endpoint
- Containerized deployment

---

## 👥 Team – WEGO

1. **Rohit Appadi**
2. **Karan Pandit**
3. **Mahesh Panda**

Project developed for Digital Business Management.


---
## 🔎 Project Preview

**POWER BI**
<img width="1119" height="630" alt="image" src="https://github.com/user-attachments/assets/4186e400-a472-46d9-803a-b505fdad2068" />

---

**WEB INTERFACE**
<img width="1600" height="800" alt="image" src="https://github.com/user-attachments/assets/b27423bb-0aeb-41cd-89d0-f637ddbeed1e" />

---

**[🚀 Try the Live Churn Prediction App]** 
https://customer-churn-app--rohitappadi.replit.app

