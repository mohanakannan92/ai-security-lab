import time
import math

RISK_SCORE = {
    "low": 1,
    "medium": 3,
    "high": 5
}

DECAY_LAMBDA = 0.05  # tune this

def analyze_sequence(session):
    intents = session["intents"]
    risks = session["risks"]
    timestamps = session.get("timestamps", [time.time()] * len(session["risks"]))

    escalation_score = 0
    flags = []

    current_time = time.time()

    decayed_history_score = 0

    for i in range(len(risks)):
        age = current_time - timestamps[i]

        # 🔥 exponential decay
        weight = math.exp(-DECAY_LAMBDA * age)

        risk_score = RISK_SCORE.get(risks[i], 1)

        decayed_history_score += risk_score * weight

    # 🔥 interpret accumulated behavior
    if decayed_history_score > 5:
        escalation_score += 2
        flags.append("recent_risk_accumulation")

    # -----------------------------
    # Existing logic (keep this)
    # -----------------------------

    if len(intents) >= 3:
        if intents[-3:] == ["benign", "probing", "sensitive"]:
            escalation_score += 2
            flags.append("intent_escalation")

    if len(intents) >= 2:
        if intents[-1] == "malicious" and intents[-2] in ["probing", "sensitive"]:
            escalation_score += 2
            flags.append("malicious_followup")

    if intents.count("probing") >= 3:
        escalation_score += 2
        flags.append("repeated_probing")

    if intents.count("sensitive") >= 2:
        escalation_score += 2
        flags.append("repeated_sensitive_requests")

    if risks.count("high") >= 2:
        escalation_score += 3
        flags.append("persistent_high_risk_behavior")

    return escalation_score, flags