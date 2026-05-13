def detect_multi_step_attack(text: str) -> dict:
    """
    Detect multi-step prompt injection attempts.
    """

    lowered = text.lower()

    step_markers = [
        "first",
        "then",
        "after that",
        "next",
        "step 1",
        "step 2",
        "finally"
    ]

    dangerous_terms = [
        "ignore",
        "disregard",
        "override",
        "reveal",
        "system prompt",
        "hidden instructions",
        "developer mode",
        "admin mode"
    ]

    found_steps = [marker for marker in step_markers if marker in lowered]
    found_danger = [term for term in dangerous_terms if term in lowered]

    is_multi_step = len(found_steps) > 0 and len(found_danger) > 0

    return {
        "is_multi_step_attack": is_multi_step,
        "step_markers": found_steps,
        "dangerous_terms": found_danger
    }