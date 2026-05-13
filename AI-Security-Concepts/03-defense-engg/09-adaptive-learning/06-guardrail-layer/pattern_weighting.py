import re
from pattern_store import load_patterns
from confidence_engine import calculate_confidence

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

    # New high-risk system leakage patterns
    r"system.*prompt": 5,
    r"hidden.*system": 5,
    r"hidden.*prompt": 5,
    r"show.*hidden": 5,
    r"developer.*instruction": 5,
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

    dynamic_patterns = load_patterns()

    base_score, matches = get_pattern_score(query)
    combo_score, combos = get_combo_score(query)

    # 🔥 Dynamic scoring
    dynamic_score = 0
    dynamic_matches = []

    DYNAMIC_STOPWORDS = {
        "what", "when", "where", "which", "your", "you", "are",
        "following", "about", "tell", "explain", "please", "can",
        "could", "would", "should", "this", "that", "with"
    }

    # ✅ MUST be inside function
    for word in query.split():
        if word in DYNAMIC_STOPWORDS:
            continue

        if word in dynamic_patterns:
            dynamic_score += dynamic_patterns[word]
            dynamic_matches.append(word)

    total_score = normalize_score(base_score, combo_score, matches) + dynamic_score
    risk = evaluate_risk(total_score)

    confidence = calculate_confidence(
    total_score,
    matches,
    combos,
    dynamic_matches
)

    if risk == "high" and confidence >= 0.7:
        action = "block"
        response = "I cannot provide details about internal system behavior or policies."

    elif risk == "high" and confidence < 0.7:
        action = "guard"
        response = "This request appears sensitive. I can only provide general information."

    elif risk == "medium":
        action = "guard"
        response = "I can provide general information, but not internal system details."

    else:
        action = "allow"
        response = None

    return {
    "query": query,
    "score": total_score,
    "confidence": round(confidence, 2),   # 🔥 NEW confidense added
    "risk": risk,
    "matches": matches,
    "combos": combos,
    "dynamic_matches": dynamic_matches,
    "action": action,
    "response": response,
}


    # Combine all scores
    total_score = normalize_score(base_score, combo_score, matches) + dynamic_score
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