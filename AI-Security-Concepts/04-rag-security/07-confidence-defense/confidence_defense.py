# confidence_defense.py

import re


# -------------------------------
# Pattern Weights (IMPORTANT)
# -------------------------------
PATTERN_WEIGHTS = {

    # 🔴 Strong signals (3)
    r"internal.*rules": 3,
    r"system.*rules": 3,
    r"reveal.*system": 3,
    r"system.*prompt": 3,

    # 🟠 Medium signals (2)
    r"how.*work": 2,
    r"how.*decide": 2,
    r"decision.*process": 2,
    r"internal.*safeguards": 2,
    r"overview.*safeguards": 2,          # NEW
    r"explain.*safeguards": 2,           # NEW

    # 🟡 Weak signals (BUT important → upgrade weight)
    r"what.*rules": 2,                   # 🔥 increased
    r"guidelines": 2,                    # 🔥 increased
    r"policies": 2,                      # 🔥 increased
}


# -------------------------------
# Normalize Query
# -------------------------------
def normalize_query(query):
    query = re.sub(r"[^\w\s]", "", query)
    query = re.sub(r"\s+", " ", query)
    return query.lower().strip()


# -------------------------------
# Score Calculation
# -------------------------------
def calculate_score(query):
    normalized = normalize_query(query)

    score = 0
    matched_patterns = []

    for pattern, weight in PATTERN_WEIGHTS.items():
        if re.search(pattern, normalized):
            score += weight
            matched_patterns.append(pattern)

    return score, matched_patterns


# -------------------------------
# Risk Classification
# -------------------------------
def classify_risk(score):
    if score >= 3:
        return "high"
    elif score >= 1:
        return "medium"
    else:
        return "low"

# -------------------------------
# Decision Engine
# -------------------------------
def confidence_guard(query):
    score, matches = calculate_score(query)
    risk = classify_risk(score)

    # -------------------------------
    # Decision Logic
    # -------------------------------
    if risk == "high":
        return {
            "action": "block",
            "risk": risk,
            "score": score,
            "matches": matches,
            "response": "I cannot provide details about internal system behavior or policies."
        }

    elif risk == "medium":
        return {
            "action": "guard",
            "risk": risk,
            "score": score,
            "matches": matches,
            "response": "I can provide general information, but not internal system details."
        }

    return {
        "action": "allow",
        "risk": risk,
        "score": score,
        "matches": matches,
        "response": None
    }