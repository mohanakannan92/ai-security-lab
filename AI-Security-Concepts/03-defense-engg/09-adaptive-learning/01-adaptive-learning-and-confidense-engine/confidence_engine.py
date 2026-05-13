def calculate_confidence(score, matches, combos, dynamic_matches):
    confidence = 0

    # 🔹 Strong static patterns
    if len(matches) > 0:
        confidence += 0.4

    # 🔹 Combo patterns (multi-signal = stronger)
    if len(combos) > 0:
        confidence += 0.3

    # 🔹 Learned patterns (adaptive signals)
    if len(dynamic_matches) > 0:
        confidence += 0.2

    # 🔹 Score strength
    if score >= 10:
        confidence += 0.2
    elif score >= 5:
        confidence += 0.1

    # 🔒 Cap confidence
    return min(confidence, 1.0)