# ai_semantic_defense.py

import re


# -------------------------------
# 🧠 Intent Categories
# -------------------------------
SENSITIVE_INTENTS = [
    "internal_rules",
    "system_behavior",
    "decision_process",
    "security_policy"
]


# -------------------------------
# 🧠 Semantic Pattern Groups
# -------------------------------
INTENT_PATTERNS = {
    "internal_rules": [
        r"what.*rules",
        r"internal.*rules",
        r"system.*rules",
        r"guidelines.*follow"
    ],

    "system_behavior": [
        r"how.*work",
        r"how.*operate",
        r"internal.*safeguards",
        r"ensure.*safe.*behavior"
    ],

    "decision_process": [
        r"how.*decide",
        r"how.*choose",
        r"decision.*process",
        r"reasoning.*process"
    ],

    "security_policy": [
        r"what.*policies",
        r"security.*controls",
        r"compliance",
        r"rules.*enforced"
    ]
}


# -------------------------------
# 🧠 Normalize Query
# -------------------------------
def normalize_query(query):
    query = re.sub(r"[^\w\s]", "", query)
    query = re.sub(r"\s+", " ", query)
    return query.lower().strip()


# -------------------------------
# 🧠 Intent Detection Engine
# -------------------------------
def detect_intent(query):
    normalized = normalize_query(query)

    detected_intents = []

    for intent, patterns in INTENT_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, normalized):
                detected_intents.append(intent)
                break

    return detected_intents


# -------------------------------
# 🧠 Risk Scoring
# -------------------------------
def calculate_risk(intents):
    if not intents:
        return "low"

    if len(intents) >= 2:
        return "high"   # multiple signals = strong attack

    if any(intent in SENSITIVE_INTENTS for intent in intents):
        return "high"

    return "medium"


# -------------------------------
# 🛡️ Final Decision Engine
# -------------------------------
def ai_semantic_guard(query):
    intents = detect_intent(query)
    risk = calculate_risk(intents)

    if risk == "high":
        return {
            "action": "block",
            "response": "I cannot provide details about internal system behavior or policies."
        }

    return {
        "action": "allow",
        "response": None
    }