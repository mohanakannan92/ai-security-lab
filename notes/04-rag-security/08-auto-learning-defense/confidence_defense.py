import re
from auto_learning_engine import learn_from_logs


# -------------------------------
# Normalize text
# -------------------------------
def normalize(text):
    text = re.sub(r"[^\w\s]", "", text.lower())
    return text


# -------------------------------
# Load dynamic learned patterns
# -------------------------------
def get_learned_patterns():
    try:
        learned_words = learn_from_logs("attack_logs.csv")
    except Exception:
        learned_words = []

    # Convert words → regex patterns
    return [rf".*{word}.*" for word in learned_words]


# -------------------------------
# Base patterns (manual rules)
# -------------------------------
BASE_PATTERNS = {
    r"internal.*rules": 2,
    r"how.*decide": 2,
    r"internal.*safeguards": 2,
    r"explain.*safeguards": 2,
    r"overview.*safeguards": 2,
    r"decision.*process": 2,
    r"system.*behavior": 2,
    r"what.*rules": 2,
}


# -------------------------------
# Confidence Guard Engine
# -------------------------------
def confidence_guard(query):
    normalized_query = normalize(query)

    score = 0
    matches = []

    # -------------------------------
    # 1. Check base patterns
    # -------------------------------
    for pattern, weight in BASE_PATTERNS.items():
        if re.search(pattern, normalized_query):
            score += weight
            matches.append(pattern)

    # -------------------------------
    # 2. Check learned patterns
    # -------------------------------
    learned_patterns = get_learned_patterns()

    for pattern in learned_patterns:
        if re.search(pattern, normalized_query):
            score += 1   # lower weight than base rules
            matches.append(pattern)

    # -------------------------------
    # 3. Risk classification
    # -------------------------------
    if score >= 4:
        risk = "high"
        action = "block"
        response = "I cannot provide details about internal system behavior or policies."

    elif score >= 2:
        risk = "medium"
        action = "guard"
        response = "I can provide general information, but not internal system details."

    else:
        risk = "low"
        action = "allow"
        response = None

    # -------------------------------
    # 4. Return structured result
    # -------------------------------
    return {
        "query": query,
        "risk": risk,
        "score": score,
        "matches": matches,
        "action": action,
        "response": response
    }