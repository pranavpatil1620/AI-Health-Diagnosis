# AI Health Diagnosis System

A web-based health symptom assessment project built with **Python, Flask, and Experta**. Users enter symptom information and the application applies rule-based logic to display an indicative result, a risk level, and general recommendations.

> **Medical disclaimer:** This project is for educational demonstration only. It is not a medical device and does not provide a reliable medical diagnosis. Do not use its results to make medical decisions. Consult a qualified healthcare professional for health concerns and seek urgent care for severe or emergency symptoms.

## Overview

The application combines a Flask web interface with an Experta rule-based knowledge engine. It evaluates a limited set of symptoms and returns an indicative result based on rules defined in the project.

## Features

- Web interface for entering symptom information.
- Rule-based symptom assessment using Experta.
- Indicative condition result and configured confidence value.
- Simple risk scoring based on selected symptoms.
- General guidance associated with the result.
- Separate application and diagnosis logic.

## Technology Stack

| Component | Technology |
|---|---|
| Programming language | Python |
| Web framework | Flask |
| Rule-based engine | Experta |
| Frontend | HTML templates, CSS, and static assets |
| Local development | Python virtual environment |

## Repository Structure

```text
AI-Health-Diagnosis/
├── static/             # CSS, images, and other static assets
├── templates/          # HTML templates used by Flask
├── app.py              # Flask application and symptom/risk workflow
├── diagnosis.py        # Experta facts and diagnosis rules
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

The repository also contains `.idea/` and `__pycache__/`. `.idea/` contains IDE-specific settings and `__pycache__/` contains generated Python cache files; neither is required to run the application. Consider removing `__pycache__/` from Git and adding it to `.gitignore`.

## Requirements

- Python installed on your computer
- `pip`
- A web browser

Dependencies listed in `requirements.txt`:
- Flask
- Experta
- Gunicorn (for compatible deployment environments)

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/pranavpatil1620/AI-Health-Diagnosis.git
cd AI-Health-Diagnosis
```

### 2. Create and activate a virtual environment

**Windows (Command Prompt):**

```bat
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Start the application

```bash
python app.py
```

Open the local address shown in the terminal (commonly `http://127.0.0.1:5000/`).

If installation fails, check the Python version and compatibility of the packages listed in `requirements.txt`.

## How It Works

1. The user opens the home page and submits the symptom form.
2. The Flask route receives the submitted values.
3. The application calculates a simple symptom-based risk score.
4. The Experta knowledge engine evaluates the configured rules.
5. The results page displays the rule-based result, risk level, confidence value, and general recommendation.

The result is limited to the symptoms and rules implemented in this project. The displayed confidence value is not a clinically validated probability.

## Limitations

- The rules cover only a small set of symptoms and conditions.
- The system does not replace medical examination, history, testing, or professional judgement.
- Rule outputs may be incomplete or incorrect for real-world health situations.
- Do not enter or publish sensitive personal health information in a public demo.

## Future Improvements

- Add broader, medically reviewed symptom rules.
- Improve input validation and error handling.
- Improve responsive and accessible interface design.
- Add automated tests for diagnosis and risk-scoring rules.
- Add emergency-symptom warnings and privacy protections.

## License

No open-source license is currently specified. Unless a license is added, users should not assume they have permission to reuse, modify, or redistribute this project.
