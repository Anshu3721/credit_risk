import streamlit as st
import pandas as pd
import requests

# FastAPI backend URL
API_URL = "http://localhost:8000/predict_score"

st.set_page_config(page_title="Credit Risk Scoring App", layout="centered")

st.title("💳 Credit Risk Prediction")
st.write("Enter applicant data to predict credit risk. The data will be sent to a FastAPI backend for scoring.")

# Input form
with st.form("prediction_form"):
    RevolvingUtilizationOfUnsecuredLines = st.number_input(
        "Revolving Utilization of Unsecured Lines",
        min_value=0.0,
        value=0.3,
        step=0.01,
        help="How much of the available credit is being used. Example: 0.3 means 30% used."
    )

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=35,
        step=1,
        help="Applicant's age in years. Example: 35."
    )

    DebtRatio = st.number_input(
        "Debt Ratio",
        min_value=0.0,
        value=0.5,
        step=0.01,
        help="Portion of monthly income used to pay debts. Example: 0.5 means 50%."
    )

    MonthlyIncome = st.number_input(
        "Monthly Income (in currency)",
        min_value=0.0,
        value=5000.0,
        step=100.0,
        help="Total monthly income before any deductions. Example: 5000."
    )

    NumberOfOpenCreditLinesAndLoans = st.number_input(
        "Number of Open Credit Lines and Loans",
        min_value=0,
        value=5,
        step=1,
        help="Total number of active loans and credit cards. Example: 5."
    )

    NumberOfDependents = st.number_input(
        "Number of Dependents",
        min_value=0,
        value=1,
        step=1,
        help="Number of family members supported financially. Example: 1."
    )

    total_delinquencies = st.number_input(
        "Total Missed Payments",
        min_value=0,
        value=0,
        step=1,
        help="Number of times payments were missed in the past. Example: 0."
    )

    has_any_delinquency = st.selectbox(
        "Any Missed Payment History?",
        options=[0, 1],
        index=0,
        help="Select 1 if there was any missed payment before, else 0."
    )

    max_delinquency_duration = st.number_input(
        "Longest Missed Payment Period (days)",
        min_value=0.0,
        value=0.0,
        step=1.0,
        help="Longest time (in days) a payment was overdue. Example: 0 or 90."
    )

    submitted = st.form_submit_button("Predict")

# Prediction logic
if submitted:
    input_data = {
        'RevolvingUtilizationOfUnsecuredLines': RevolvingUtilizationOfUnsecuredLines,
        'age': age,
        'DebtRatio': DebtRatio,
        'MonthlyIncome': MonthlyIncome,
        'NumberOfOpenCreditLinesAndLoans': NumberOfOpenCreditLinesAndLoans,
        'NumberOfDependents': NumberOfDependents,
        'total_delinquencies': total_delinquencies,
        'has_any_delinquency': has_any_delinquency,
        'max_delinquency_duration': max_delinquency_duration
    }

    st.write("Sending the following data to FastAPI backend:")
    st.json(input_data)

    try:
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            result = response.json()

            # Show prediction results nicely
            if result["prediction"] == 1:
                st.error(f"❌ Prediction: High Risk of Default")
            else:
                st.success(f"✅ Prediction: Low Risk of Default")

            st.markdown(f"**Risk Score:** `{result['risk_score']:.2f}`")
            st.markdown(f"**Risk Level:** {result['risk_level']}")

        else:
            st.error(f"API Error {response.status_code}: {response.text}")

    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to FastAPI backend: {e}")
