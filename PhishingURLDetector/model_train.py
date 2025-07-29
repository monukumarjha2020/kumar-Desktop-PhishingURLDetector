import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# Sample data
data = {
    "url_length": [20, 85, 33, 70, 17],
    "has_https": [1, 0, 1, 0, 1],
    "has_at": [0, 1, 0, 1, 0],
    "has_dash": [0, 1, 0, 1, 0],
    "label": [0, 1, 0, 1, 0]  # 0: Safe, 1: Phishing
}

df = pd.DataFrame(data)
X = df[["url_length", "has_https", "has_at", "has_dash"]]
y = df["label"]

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, "model.pkl")
print("Model trained and saved as model.pkl")
