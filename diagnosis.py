from experta import Fact, KnowledgeEngine, Rule


class Symptom(Fact):
    """Stores patient symptoms."""
    pass


class HealthDiagnosis(KnowledgeEngine):

    def __init__(self):
        super().__init__()
        self.diagnosis = "Unknown"
        self.confidence = 0
        self.risk = "Unknown"

    # FLU
    @Rule(
        Symptom(fever="yes"),
        Symptom(cough="yes"),
        Symptom(body_pain="yes")
    )
    def flu(self):
        self.diagnosis = "Flu"
        self.confidence = 90
        self.risk = "Medium"

    # COMMON COLD
    @Rule(
        Symptom(fever="no"),
        Symptom(cough="yes"),
        Symptom(body_pain="no")
    )
    def common_cold(self):
        self.diagnosis = "Common Cold"
        self.confidence = 85
        self.risk = "Low"

    # VIRAL FEVER
    @Rule(
        Symptom(fever="yes"),
        Symptom(cough="no"),
        Symptom(body_pain="yes")
    )
    def viral_fever(self):
        self.diagnosis = "Viral Fever"
        self.confidence = 85
        self.risk = "Medium"

    # FEVER
    @Rule(
        Symptom(fever="yes"),
        Symptom(cough="no"),
        Symptom(body_pain="no")
    )
    def fever_only(self):
        self.diagnosis = "Fever"
        self.confidence = 75
        self.risk = "Medium"

    # THROAT INFECTION
    @Rule(
        Symptom(fever="no"),
        Symptom(cough="yes"),
        Symptom(body_pain="yes")
    )
    def throat_infection(self):
        self.diagnosis = "Possible Throat Infection"
        self.confidence = 70
        self.risk = "Medium"

    # HEALTHY
    @Rule(
        Symptom(fever="no"),
        Symptom(cough="no"),
        Symptom(body_pain="no")
    )
    def healthy(self):
        self.diagnosis = "Healthy"
        self.confidence = 95
        self.risk = "Low"