# kumar-Desktop-PhishingURLDetector
This is a simple web application to detect phishing URLs using basic machine learning and URL feature analysis.

# 🔐 Phishing URL Detection - Flask App

This is a simple web application to detect phishing URLs using basic machine learning and URL feature analysis.

---

## 🚀 How to Run This Project (Next Time)

### ✅ Step 1: Open the Project Folder
```
C:\Users\Monu Kumar\Desktop\PhishingURLDetector
```

---

### ✅ Step 2: Activate Virtual Environment (Important)
Run this command in your terminal:
```
.env\Scriptsctivate
```
You should see `(venv)` appear on the left of your terminal line.

---

### ✅ Step 3: Run the Web App
```
python app.py
```

Then open this URL in your browser:
```
http://127.0.0.1:5000/
```

---

## ❗ Optional: Retrain the Model
You only need to run this if:
- You deleted the `model.pkl` file
- You want to train with new data

Run:
```
python model_train.py
```

---

## 📦 Dependencies (Only if you create a new environment)
```
pip install flask scikit-learn pandas joblib
```

---

## 📁 Project Structure

```
PhishingURLDetector/
├── app.py              # Flask application
├── model_train.py      # Script to train the ML model
├── model.pkl           # Trained model file (auto-generated)
├── templates/
│   └── index.html      # Frontend HTML form
├── venv/               # Virtual environment
└── README.md           # This file
```

---

### 🛡️ Do NOT Use Real Malicious Links
Use dummy test URLs only (e.g., `http://login-fake.com`, `https://safe-site.com`).
Do not attempt to visit or use live phishing URLs.

---

## 📞 Need Help?
Ping me anytime! 😉

