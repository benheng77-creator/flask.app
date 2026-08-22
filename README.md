# Linear Regression Flask App

An educational Flask application that trains a simple linear-regression model to predict an exam score from study hours. It includes a browser interface and a JSON API suitable for Power Automate or Power Apps demonstrations.

## Features

- trains and persists a small linear-regression model
- serves a browser form for predictions
- exposes a `POST /predict` JSON endpoint
- runs locally with Python and Flask

## Project structure

```text
flask.app/
├── models/
│   └── linear_regression_model.joblib
├── templates/
│   └── index.html
├── .gitignore
├── .python-version
├── app.py
├── data.csv
├── README.md
├── requirements.txt
└── train_model.py
```

## Setup

```bash
python -m venv .venv
```

Activate the environment:

```bash
# macOS or Linux
source .venv/bin/activate

# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run

Train the model:

```bash
python train_model.py
```

Start Flask:

```bash
python app.py
```

Open `http://127.0.0.1:5000`.

## API

Request:

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"study_hours": 5}'
```

Example response:

```json
{
  "study_hours": 5.0,
  "exam_score": 60.5
}
```

## Security

Please report vulnerabilities privately through this repository's **Security** tab. See [SECURITY.md](SECURITY.md).
