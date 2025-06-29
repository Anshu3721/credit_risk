📊 Credit Risk Scoring App
A complete machine learning project with FastAPI backend and Streamlit frontend, containerized with Docker.
Predicts credit default risk from applicant financial data.

✨ Features
✅ FastAPI backend for model serving
✅ Streamlit frontend UI for user input and visualization
✅ Pretrained machine learning model (Random Forest)
✅ Scikit-Learn StandardScaler for input preprocessing
✅ Docker & Docker Compose support for easy deployment
✅ Clean separation of backend and frontend services

⚙️ Architecture
css
Copy
Edit
credit_risk_project/
├── docker-compose.yml
├── backend/
│   ├── main.py
│   ├── schema.py
│   ├── model/
│   │   ├── risk_model.pkl
│   │   └── scaler.pkl
│   ├── requirements.txt
│   └── Dockerfile
└── frontend/
    ├── streamlit_app.py
    ├── requirements.txt
    └── Dockerfile
Backend: FastAPI app exposing /predict_score endpoint.

Frontend: Streamlit app with user-friendly form sending data to FastAPI.

Docker Compose: Spins up both services with one command.

✅ Requirements
Python 3.10 / 3.11 (for local dev)

Docker & Docker Compose

🚀 Getting Started
🟣 1️⃣ Clone the Repo
bash
Copy
Edit
git clone https://github.com/yourusername/credit_risk_project.git
cd credit_risk_project
🟢 2️⃣ Running Locally without Docker
🧭 Backend (FastAPI)
bash
Copy
Edit
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 8000
✅ Open docs at http://127.0.0.1:8000/docs

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
✅ Visit http://localhost:8501

🟡 3️⃣ Running with Docker Compose (Recommended)
Build & Start Both Services:
bash
Copy
Edit
docker-compose up --build
✅ FastAPI: http://localhost:8000/docs
✅ Streamlit: http://localhost:8501

🟠 4️⃣ Stopping and Cleaning Up
bash
Copy
Edit
docker-compose down
⚡️ Model & Scaler
The model and scaler files are saved in backend/model/.

⚠️ These files can be large. It is recommended to ignore them in Git using:

bash
Copy
Edit
backend/model/
For sharing large models, use Git LFS.

✅ Example .gitignore
bash
Copy
Edit
__pycache__/
*.pyc
.venv/
venv/
myvenv/
.vscode/
.idea/

# Model artifacts
backend/model/
🧰 Technologies Used
Python 3.11

FastAPI

Uvicorn

Streamlit

Scikit-Learn

Pandas, NumPy

Docker

Docker Compose

⚙️ How It Works
1️⃣ User opens Streamlit UI.
2️⃣ Enters applicant details in the form.
3️⃣ Streamlit sends a JSON POST request to FastAPI.
4️⃣ FastAPI:

Scales the input using StandardScaler

Loads the trained RandomForestClassifier

Predicts risk score and class
5️⃣ Response sent back to Streamlit.
6️⃣ Streamlit displays:

Prediction (High Risk / Low Risk)

Risk Score

✅ Example JSON request
bash
Copy
Edit
POST /predict_score

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
✅ Response:

json
Copy
Edit
{
  "prediction": 0,
  "risk_score": 0.12,
  "risk_level": "Low Risk"
}
⚠️ Troubleshooting
✅ Error pushing large .pkl file to GitHub?

GitHub blocks files >100MB.

Solution: Remove from history:

bash
Copy
Edit
pip install git-filter-repo
git filter-repo --path backend/model/risk_model.pkl --invert-paths
git push origin main --force
✅ Or use Git LFS:

sql
Copy
Edit
git lfs install
git lfs track "*.pkl"
git add .gitattributes
git commit -m "Track models with LFS"
git push origin main
✅ License
MIT License.

✅ Author
👤 Anshu Kumar

If you want, you can customize this further with:

Badges

Screenshots

Credits

🎯 TL;DR Usage
Local (dev):

bash
Copy
Edit
# Backend
cd backend
uvicorn main:app --reload

# Frontend
cd frontend
streamlit run streamlit_app.py
Docker (production):

bash
Copy
Edit
docker-compose up --build
