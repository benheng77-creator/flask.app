import os

import joblib
import pandas as pd
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

# Resolve paths relative to this file so app works regardless of CWD
BASEDIR = os.path.abspath(os.path.dirname(__file__))
MODEL_FILE = os.path.join(BASEDIR, "models", "linear_regression_model.joblib")

# Load saved model
if not os.path.exists(MODEL_FILE):
    raise FileNotFoundError(
        f"Model file not found at {MODEL_FILE}. Run train_model.py to create it."
    )

model_package = joblib.load(MODEL_FILE)

model = model_package["model"]
feature_column = model_package["feature_column"]
target_column = model_package["target_column"]

# Create Flask app with explicit templates folder
app = Flask(__name__, template_folder=os.path.join(BASEDIR, "templates"))
CORS(app)


# Webpage route
# This is for browser testing
@app.route("/", methods=["GET", "POST"])
def index():
    study_hours = None
    exam_score = None
    error = None

    if request.method == "POST":
        try:
            study_hours = float(request.form["study_hours"])

            input_data = pd.DataFrame({
                feature_column: [study_hours]
            })

            exam_score = model.predict(input_data)[0]
            exam_score = round(exam_score, 2)

        except ValueError:
            error = "Please enter a valid number."

    return render_template(
        "index.html",
        study_hours=study_hours,
        exam_score=exam_score,
        error=error
    )


# API route
# This is for Power Automate / Power Apps
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        study_hours = float(data["study_hours"])

        input_data = pd.DataFrame({
            feature_column: [study_hours]
        })

        exam_score = model.predict(input_data)[0]
        exam_score = round(exam_score, 2)

        return jsonify({
            "study_hours": study_hours,
            "exam_score": exam_score
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
