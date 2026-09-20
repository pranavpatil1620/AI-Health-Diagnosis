from flask import Flask, render_template, request
from diagnosis import HealthDiagnosis, Symptom

app = Flask(__name__)


def calculate_risk(symptoms):

    score = 0

    if symptoms["fever"] == "yes":
        score += 2

    if symptoms["cough"] == "yes":
        score += 1

    if symptoms["body_pain"] == "yes":
        score += 1

    if symptoms["headache"] == "yes":
        score += 1

    if symptoms["sore_throat"] == "yes":
        score += 1

    if symptoms["fatigue"] == "yes":
        score += 1

    if score <= 2:
        risk = "LOW"
    elif score <= 4:
        risk = "MEDIUM"
    else:
        risk = "HIGH"

    return risk, score


def get_recommendation(diagnosis, risk):

    if risk == "HIGH":
        return "Your symptoms indicate a higher risk. Please consult a qualified doctor as soon as possible."

    recommendations = {
        "Flu":
            "Take proper rest, drink plenty of fluids and consult a doctor if symptoms become severe.",

        "Common Cold":
            "Drink warm fluids, take adequate rest and maintain good hydration.",

        "Viral Fever":
            "Take rest, drink plenty of fluids and monitor your temperature.",

        "Fever":
            "Monitor your temperature and stay hydrated. Consult a doctor if fever continues.",

        "Possible Throat Infection":
            "Drink warm water, take rest and consult a doctor if symptoms continue.",

        "Healthy":
            "You currently show no major symptoms. Continue maintaining a healthy lifestyle."
    }

    return recommendations.get(
        diagnosis,
        "Symptoms are not sufficient for a clear diagnosis. Please consult a doctor."
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/diagnose", methods=["POST"])
def diagnose():

    name = request.form.get("name")

    symptoms = {
        "fever": request.form.get("fever"),
        "cough": request.form.get("cough"),
        "body_pain": request.form.get("body_pain"),
        "headache": request.form.get("headache"),
        "sore_throat": request.form.get("sore_throat"),
        "fatigue": request.form.get("fatigue")
    }

    # AI Risk Calculation
    risk, score = calculate_risk(symptoms)

    # Experta Engine
    engine = HealthDiagnosis()
    engine.reset()

    engine.declare(
        Symptom(
            fever=symptoms["fever"],
            cough=symptoms["cough"],
            body_pain=symptoms["body_pain"]
        )
    )

    engine.run()

    diagnosis = engine.diagnosis
    confidence = engine.confidence

    recommendation = get_recommendation(
        diagnosis,
        risk
    )

    return render_template(
        "result.html",
        name=name,
        diagnosis=diagnosis,
        confidence=confidence,
        risk=risk,
        score=score,
        recommendation=recommendation
    )


if __name__ == "__main__":
    app.run(debug=True)