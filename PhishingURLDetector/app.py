from flask import Flask, request, render_template
import joblib
import urllib.parse

app = Flask(__name__)
model = joblib.load("model.pkl")

def extract_features(url):
    features = []
    features.append(len(url))  # URL length
    features.append(1 if "https" in url else 0)
    features.append(1 if "@" in url else 0)
    features.append(1 if "-" in urllib.parse.urlparse(url).netloc else 0)
    return [features]

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        url = request.form["url"]
        features = extract_features(url)
        prediction = model.predict(features)[0]
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
