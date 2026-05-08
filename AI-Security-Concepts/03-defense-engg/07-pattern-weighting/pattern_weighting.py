import re


# -------------------------------
# 🎯 Pattern Weights
# -------------------------------
PATTERN_WEIGHTS = {
    r"what.*rules": 2,
    r"internal.*rules": 3,
    r"explain.*safeguards": 4,
    r"internal.*safeguards": 4,
    r"how.*decide": 2,
    r"overview.*safeguards": 2,
}


# -------------------------------
# 🔥 Combo Patterns (Multi-signal)
# -------------------------------
COMBO_PATTERNS = [
    (["internal", "rules"], 2),
    (["internal", "safeguards"], 2),
    (["explain", "internal"], 3),
]


# -------------------------------
# 🧠 Normalize Input
# -------------------------------
def normalize(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# -------------------------------
# 🔍 Pattern Matching
# -------------------------------
def get_pattern_score(query):
    score = 0
    matches = []

    for pattern, weight in PATTERN_WEIGHTS.items():
        if re.search(pattern, query):
            score += weight
            matches.append(pattern)

    return score, matches


# -------------------------------
# 🔥 Combo Detection
# -------------------------------
def get_combo_score(query):
    combo_score = 0
    triggered = []

    for keywords, weight in COMBO_PATTERNS:
        if all(word in query for word in keywords):
            combo_score += weight
            triggered.append("+".join(keywords))

    return combo_score, triggered


# -------------------------------
# ⚖️ Score Normalization (IMPORTANT)
# -------------------------------
def normalize_score(base_score, combo_score, matches):
    total_score = base_score + combo_score

    # 🔻 Overlap penalty (avoid double/triple counting)
    unique_matches = len(matches)
    if unique_matches > 2:
        total_score -= (unique_matches - 2)

    # 🔒 Hard cap (prevents score explosion)
    total_score = min(total_score, 10)

    return max(total_score, 0)  # ensure non-negative


# -------------------------------
# 🎯 Risk Evaluation (Tuned)
# -------------------------------
def evaluate_risk(score):
    if score >= 7:
        return "high"
    elif score >= 2:
        return "medium"
    else:
        return "low"


# -------------------------------
# 🚀 Main Guard Function
# -------------------------------
def pattern_weight_guard(query):
    query = normalize(query)

    base_score, matches = get_pattern_score(query)
    combo_score, combos = get_combo_score(query)

    total_score = normalize_score(base_score, combo_score, matches)
    risk = evaluate_risk(total_score)

    # -------------------------------
    # 🎯 Action Mapping
    # -------------------------------
    if risk == "high":
        action = "block"
        response = "I cannot provide details about internal system behavior or policies."
    elif risk == "medium":
        action = "guard"
        response = "I can provide general information, but not internal system details."
    else:
        action = "allow"
        response = None

    return {
        "query": query,
        "score": total_score,
        "risk": risk,
        "matches": matches,
        "combos": combos,
        "action": action,
        "response": response,
    }