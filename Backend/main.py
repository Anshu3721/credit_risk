from fastapi import FastAPI
from schema import ApplicantData
import pickle
import numpy as np
import os

# Build path to model/scaler
MODEL_PATH = os.path.join("model", "risk_model.pkl")
SCALER_PATH = os.path.join("model", "scaler.pkl")

# Load model and scaler
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(SCALER_PATH, "rb") as f:
    scaler = pickle.load(f)

app = FastAPI(title="Credit Risk Scoring API")

@app.get("/")
def root():
    return {"message": "Credit Risk Scoring API is running"}

@app.post("/predict_score")
def predict_score(data: ApplicantData):
    features = np.array([[ 
        data.RevolvingUtilizationOfUnsecuredLines,
        data.age,
        data.DebtRatio,
        data.MonthlyIncome,
        data.NumberOfOpenCreditLinesAndLoans,
        data.NumberOfDependents,
        data.total_delinquencies,
        data.has_any_delinquency,
        data.max_delinquency_duration
    ]])

    features_scaled = scaler.transform(features)
    proba = model.predict_proba(features_scaled)[0][1]
    prediction = model.predict(features_scaled)[0]
    risk_level = "High Risk" if prediction == 1 else "Low Risk"

    return {
        "prediction": int(prediction),
        "risk_score": round(proba, 4),
        "risk_level": risk_level
    }
