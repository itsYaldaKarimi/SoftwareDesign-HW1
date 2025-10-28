# 🚀 CI/CD Pipeline for Flask Application

## 🧩 Overview
This project demonstrates a **Continuous Integration (CI)** and **Continuous Deployment (CD)** pipeline using **GitHub Actions** for a simple **Flask application**.  
Every time code is pushed to the repository, GitHub automatically installs dependencies, runs tests, and verifies that the project builds successfully.

---

## ⚙️ Technologies Used
- **Python 3.10**
- **Flask**
- **pytest** (for automated testing)
- **GitHub Actions** (for CI/CD automation)

---

## 🧱 Project Structure
SoftwareDesign/
│
├── YaldaKarimi_simple_profile_flask.py # Main Flask application
├── requirements.txt # Project dependencies
├── test_app.py # Unit test for Flask app
└── .github/
└── workflows/
└── ci.yml # GitHub Actions CI/CD configuration

yaml
Copy code

---

## 🔄 CI Pipeline Workflow

### Trigger
The workflow runs automatically on:
- Every `push` to the `main` branch  
- Every `pull request` to the `main` branch

### Steps
1. **Checkout Repository**
   ```yaml
   - uses: actions/checkout@v4
Set up Python Environment

yaml
Copy code
- uses: actions/setup-python@v5
  with:
    python-version: '3.10'
Install Dependencies

yaml
Copy code
- run: pip install -r requirements.txt
Run Tests

yaml
Copy code
- run: pytest -v
Build Confirmation

yaml
Copy code
- run: echo "✅ Flask app build successful!"
✅ Test Example (test_app.py)
python
Copy code
from YaldaKarimi_simple_profile_flask import app

def test_home_page():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
🧪 Result
When all tests pass, the pipeline completes successfully and displays:

Copy code
✅ Flask app build successful!
If any test fails, the pipeline is marked as failed, and the error log is shown in GitHub Actions.

🚀 Possible Next Step (CD)
To enable full Continuous Deployment, the app can be automatically deployed to:

Render, Railway, or Heroku
after the CI workflow passes successfully.

👩‍💻 Author
itsYaldaKarimi
GitHub CI/CD Practice Project – Software Design Course
