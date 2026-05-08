import re
import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "attack_logs.csv")


# 🔒 Static base patterns
BASE_PATTERNS = {
    r"what.*rules": 2,
    r"how.*decide": 2,
    r"internal.*rules": 4,
    r"internal.*safeguards": 4,
    r"explain.*safeguards": 3,
}


# ⚡ Combo patterns (high signal)
COMBO_PATTERNS = {
    ("internal", "rules"): 3,
    ("internal", "safeguards"): 4,
    ("explain", "internal"): 2,
}


# 🚀 Convert learned words → safe regex patterns
def build_dynamic_patterns(learned_patterns):
    dynamic = {}

    for word, freq in learned_patterns.items():

        # ✅ Word boundary regex (prevents substring issues)
        pattern = rf"\b{word}\b"

        # 🎯 Controlled weighting (avoid overblocking)
        if freq >= 5:
            weight = 3
        elif freq >= 3:
            weight = 2
        else:
            weight = 1   # 👈 reduced impact

        dynamic[pattern] = weight

    return dynamic


def detect_with_patterns(query, learned_patterns=None):
    query = query.lower()

    patterns = BASE_PATTERNS.copy()

    # 🔥 Inject learned patterns
    if learned_patterns:
        patterns.update(build_dynamic_patterns(learned_patterns))

    score = 0
    matches = []
    used_words = set()

    # 🔍 Pattern matching
    for pattern, weight in patterns.items():
        if re.search(pattern, query):
            score += weight
            matches.append(pattern)

            words = re.findall(r'\b[a-zA-Z]{4,}\b', pattern)
            used_words.update(words)

    # ⚡ Combo detection
    combos = []
    for (w1, w2), bonus in COMBO_PATTERNS.items():
        if w1 in query and w2 in query:
            score += bonus
            combos.append(f"{w1}+{w2}")

    # ⚠️ Overlap penalty
    if len(used_words) < len(matches):
        score -= 1

    # 🔒 Cap score
    score = min(score, 10)

    # 🎯 Risk classification (tuned thresholds)
    if score >= 7:
        risk = "high"
        action = "block"
        response = "I cannot provide details about internal system behavior or policies."
    elif score >= 3:
        risk = "medium"
        action = "guard"
        response = "I can provide general information, but not internal system details."
    else:
        risk = "low"
        action = "allow"
        response = None

    # 📝 Log event
    log_event(query, score, risk, action)

    return {
        "score": score,
        "risk": risk,
        "matches": matches,
        "combos": combos,
        "action": action,
        "response": response
    }


# 🧾 Logging system (self-contained CSV)
def log_event(query, score, risk, action):
    print("📝 Logging:", query)

    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["query", "score", "risk", "action"])

        writer.writerow([query, score, risk, action])