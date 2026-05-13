# ============================================
# intent_classifier.py
# ============================================

import re

# --------------------------------------------
# Intent Categories
# --------------------------------------------

INTENT_PATTERNS = {
    "benign": [
        r"\bwhat is\b",
        r"\bexplain\b",
        r"\bhow does\b",
        r"\btutorial\b",
        r"\blearn\b",
    ],

    "probing": [
        r"\bwhat safeguards\b",
        r"\bwhat rules\b",
        r"\bhow are you protected\b",
        r"\binternal policy\b",
        r"\bsecurity mechanism\b",
    ],

    "sensitive": [
        r"\bsystem prompt\b",
        r"\binternal instructions\b",
        r"\bhidden rules\b",
        r"\bconfidential\b",
        r"\breveal prompt\b",
    ],

    "malicious": [
        r"\bignore previous instructions\b",
        r"\bbypass\b",
        r"\bjailbreak\b",
        r"\boverride\b",
        r"\ddisable safety\b",
    ]
}

# --------------------------------------------
# Intent Weights
# --------------------------------------------

INTENT_WEIGHTS = {
    "benign": 1,
    "probing": 3,
    "sensitive": 6,
    "malicious": 10
}


# ============================================
# Intent Classification Function
# ============================================

def classify_intent(user_input):
    """
    Detects user intent based on regex patterns.

    Returns:
        {
            "intent": detected_intent,
            "intent_score": score,
            "matched_patterns": []
        }
    """

    text = user_input.lower()

    detected_intent = "benign"
    highest_score = 0
    matched_patterns = []

    # ----------------------------------------
    # Check all intent categories
    # ----------------------------------------

    for intent, patterns in INTENT_PATTERNS.items():

        for pattern in patterns:

            if re.search(pattern, text):

                score = INTENT_WEIGHTS[intent]

                matched_patterns.append(pattern)

                # Keep highest severity intent
                if score > highest_score:
                    highest_score = score
                    detected_intent = intent

    return {
        "intent": detected_intent,
        "intent_score": highest_score,
        "matched_patterns": matched_patterns
    }