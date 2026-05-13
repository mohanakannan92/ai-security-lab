# ============================================
# pattern_weighting.py
# ============================================

import re
from intent_classifier import classify_intent

# --------------------------------------------
# Suspicious Pattern Weights
# --------------------------------------------

PATTERN_WEIGHTS = {
    "ignore": 4,
    "bypass": 5,
    "reveal": 5,
    "system prompt": 7,
    "hidden instructions": 8,
    "jailbreak": 10,
}

# --------------------------------------------
# Risk Thresholds
# --------------------------------------------

LOW_THRESHOLD = 4
MEDIUM_THRESHOLD = 8
HIGH_THRESHOLD = 15


# ============================================
# Pattern Score Calculation
# ============================================

def calculate_pattern_score(user_input):
    """
    Calculates weighted score based on
    suspicious keyword/pattern detection.
    """

    text = user_input.lower()

    score = 0
    matched_patterns = []

    # ----------------------------------------
    # Weighted Pattern Matching
    # ----------------------------------------

    for pattern, weight in PATTERN_WEIGHTS.items():

        # Prevent partial word matching
        regex_pattern = rf"\b{re.escape(pattern)}\b"

        if re.search(regex_pattern, text):

            score += weight
            matched_patterns.append(pattern)

    return score, matched_patterns


# ============================================
# Final Risk Evaluation
# ============================================

def evaluate_risk(user_input):
    """
    Main risk evaluation pipeline.

    Flow:
    Intent → Pattern → Score → Decision
    """

    # ----------------------------------------
    # Step 1 - Intent Classification
    # ----------------------------------------

    intent_result = classify_intent(user_input)

    intent_score = intent_result["intent_score"]

    # ----------------------------------------
    # Step 2 - Pattern Scoring
    # ----------------------------------------

    pattern_score, matched_patterns = calculate_pattern_score(user_input)

    # ----------------------------------------
    # Step 3 - Final Weighted Score
    # ----------------------------------------

    final_score = (
        intent_score * 0.4 +
        pattern_score * 0.6
    )

    # ----------------------------------------
    # Step 4 - Intelligent Escalation Logic
    # ----------------------------------------

    # Malicious intent + suspicious patterns
    # should immediately raise severity.

    if (
        intent_result["intent"] == "malicious"
        and pattern_score >= 5
    ):
        risk = "HIGH"

    # Sensitive queries with suspicious
    # patterns deserve elevated attention.

    elif (
        intent_result["intent"] == "sensitive"
        and pattern_score >= 5
    ):
        risk = "MEDIUM"

    # ----------------------------------------
    # Step 5 - Standard Threshold Logic
    # ----------------------------------------

    elif final_score >= HIGH_THRESHOLD:
        risk = "HIGH"

    elif final_score >= MEDIUM_THRESHOLD:
        risk = "MEDIUM"

    elif final_score >= LOW_THRESHOLD:
        risk = "LOW"

    else:
        risk = "SAFE"

    # ----------------------------------------
    # Step 6 - Explainable Output
    # ----------------------------------------

    return {
        "query": user_input,

        # Intent information
        "intent": intent_result["intent"],
        "intent_score": intent_score,

        # Pattern analysis
        "pattern_score": pattern_score,
        "matched_patterns": matched_patterns,

        # Final security assessment
        "final_score": round(final_score, 2),
        "risk": risk
    }