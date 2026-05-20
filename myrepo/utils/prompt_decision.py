# Dangerous patterns
BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "reveal system prompt",
    "show hidden configuration",
    "developer mode",
    "admin mode",
    "repeat everything above",
    "bypass security",
    "disable safety",
    "override rules",
]


def evaluate_prompt_risk(user_input: str) -> dict:
    """
    Simulate prompt security decision logic
    """

    normalized = user_input.lower()

    detected_patterns = []

    for pattern in BLOCKED_PATTERNS:
        if pattern in normalized:
            detected_patterns.append(pattern)

    # Decision logic
    if detected_patterns:
        return {
            "decision": "REFUSE",
            "risk_level": "HIGH",
            "matched_patterns": detected_patterns
        }

    return {
        "decision": "ALLOW",
        "risk_level": "LOW",
        "matched_patterns": []
    }