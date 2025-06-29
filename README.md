# 📊 Credit Risk Scoring App

A **production-ready machine learning application** to predict credit default risk from applicant financial data, built with a **FastAPI backend**, a **Streamlit frontend**, and containerized for effortless deployment.

---

## ✨ Features

- ✅ **FastAPI backend** for real-time prediction and model serving
- ✅ **Streamlit UI** for intuitive user input & live risk visualization
- ✅ **Pretrained ML model** (`RandomForestClassifier`)
- ✅ **Automated input scaling** with `StandardScaler`
- ✅ **Docker & Docker Compose** for one-command deployment
- ✅ **Separation of backend/frontend** for robust, scalable architecture

---

## ⚙️ Project Structure

`credit_risk_project/
├── docker-compose.yml
├── backend/
│ ├── main.py
│ ├── schema.py
│ ├── model/
│ │ ├── risk_model.pkl
│ │ └── scaler.pkl
│ ├── requirements.txt
│ └── Dockerfile
└── frontend/
├── streamlit_app.py
├── requirements.txt
└── Dockerfile`

yaml
Copy
Edit

- **Backend:** FastAPI app exposing a `/predict_score` endpoint
- **Frontend:** Streamlit app with a user-friendly input form, calls backend API
- **Docker Compose:** Orchestrates both services for local/prod use

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository


`git clone https://github.com/yourusername/credit_risk_project.git
cd credit_risk_project`


### 2️⃣ Run Locally (Without Docker)
🧭 Backend (FastAPI)
bash
Copy
Edit
`cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 8000`

Open interactive docs: http://127.0.0.1:8000/docs

🧭 Frontend (Streamlit)
Open a new terminal:

bash
Copy
Edit
cd frontend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
Access Streamlit UI: http://localhost:8501

### 3️⃣ Run with Docker Compose (Recommended)
bash
Copy
Edit
docker-compose up --build
FastAPI docs: http://localhost:8000/docs

Streamlit UI: http://localhost:8501

### 4️⃣ Stop & Clean Up
bash
Copy
Edit
docker-compose down
### ⚡️ Model & Scaler Files
The model and scaler (risk_model.pkl, scaler.pkl) are stored in backend/model/.

⚠️ Note: These files can be large!

Ignore them in Git with backend/model/ in .gitignore

For files >100MB, use Git LFS

### Example .gitignore
gitignore
Copy
Edit
__pycache__/
*.pyc
.venv/
venv/
myvenv/
.vscode/
.idea/
backend/model/

---

### 🧰 Technologies Used
Python 3.10 / 3.11

FastAPI & Uvicorn

Streamlit

Scikit-Learn, Pandas, NumPy

Docker & Docker Compose
---

### 🛠️ How It Works
User opens Streamlit UI in browser

Fills out applicant financial data form

Streamlit sends a POST request to FastAPI /predict_score

FastAPI:

Scales input with StandardScaler

Loads the trained Random Forest model

Predicts risk score & class

Response sent back to Streamlit

### Streamlit displays:

Risk Prediction: High Risk / Low Risk

Risk Score: Probability of default

---

### ✅ Example: API Usage
Request
http
Copy
Edit
POST /predict_score
Content-Type: application/json

{
  "RevolvingUtilizationOfUnsecuredLines": 0.3,
  "age": 35,
  "DebtRatio": 0.5,
  "MonthlyIncome": 5000,
  "NumberOfOpenCreditLinesAndLoans": 5,
  "NumberOfDependents": 1,
  "total_delinquencies": 0,
  "has_any_delinquency": 0,
  "max_delinquency_duration": 0
}
Response
json
Copy
Edit
{
  "prediction": 0,
  "risk_score": 0.12,
  "risk_level": "Low Risk"
}

---

### 🐞 Troubleshooting
Error pushing large model (.pkl) to GitHub?

GitHub blocks files >100MB.

Solution: Remove from repo history:

bash
Copy
Edit
pip install git-filter-repo
git filter-repo --path backend/model/risk_model.pkl --invert-paths
git push origin main --force
Or use Git LFS:

bash
Copy
Edit
git lfs install
git lfs track "*.pkl"
git add .gitattributes
git commit -m "Track models with LFS"
git push origin main


### Backend
cd backend
uvicorn main:app --reload

### Frontend
cd frontend
streamlit run streamlit_app.py


### Docker (production):
bash
Copy
Edit
docker-compose up --build

------
### 👤 Author
Your Name

### 💡 Want to Contribute?
Open to improvements, new features, and suggestions!
Feel free to open Issues or Pull Requests.
