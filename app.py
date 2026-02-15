import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Customer Churn Predictor", layout="wide")

st.title("Customer Churn Prediction System")

# Load model artifacts
model = joblib.load("models/churn_model.pkl")
scaler = joblib.load("models/scaler.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")

uploaded_file = st.file_uploader("Upload Original IBM Customer CSV", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    # Clean column names
    df.columns = df.columns.str.replace('\ufeff', '', regex=True)
    df.columns = df.columns.str.strip()

    original_df = df.copy()

    # Drop leakage columns
    drop_cols = [
        "CustomerID",
        "Count",
        "Lat Long",
        "Latitude",
        "Longitude",
        "Churn Label",
        "Churn Score",
        "CLTV",
        "Churn Reason"
    ]

    df = df.drop(columns=drop_cols, errors="ignore")

    # Separate features
    X = df.drop("Churn Value", axis=1)

    # Drop high cardinality columns
    high_cardinality = ["Country", "State", "City", "Zip Code"]
    X = X.drop(columns=high_cardinality, errors="ignore")

    # One-hot encode
    X = pd.get_dummies(X, drop_first=True)

    # Align columns
    X = X.reindex(columns=feature_columns, fill_value=0)

    # Scale
    X_scaled = scaler.transform(X)

    # Predict
    original_df["Predicted_Churn"] = model.predict(X_scaled)
    original_df["Churn_Probability"] = model.predict_proba(X_scaled)[:, 1]

    # Risk segmentation
    def risk_segment(prob):
        if prob >= 0.7:
            return "High Risk"
        elif prob >= 0.4:
            return "Medium Risk"
        else:
            return "Low Risk"

    original_df["Risk Segment"] = original_df["Churn_Probability"].apply(risk_segment)

    # Metrics display
    st.subheader("Prediction Summary")

    total_customers = len(original_df)
    high_risk = len(original_df[original_df["Risk Segment"] == "High Risk"])
    revenue_at_risk = original_df[original_df["Risk Segment"] == "High Risk"]["Monthly Charges"].sum()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Customers", total_customers)
    col2.metric("High Risk Customers", high_risk)
    col3.metric("Revenue At Risk", f"${revenue_at_risk:,.2f}")

    st.subheader("Preview of Predictions")
    st.dataframe(original_df.head(10))

    # Download button
    csv = original_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download Predictions CSV",
        data=csv,
        file_name="customer_with_predictions.csv",
        mime="text/csv"
    )