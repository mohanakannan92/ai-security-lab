def analyze_sequence(session):
    intents = session["intents"]
    risks = session["risks"]

    escalation_score = 0
    flags = []

    # 1. Intent escalation:
    # benign -> probing -> sensitive
    if len(intents) >= 3:
        if intents[-3:] == ["benign", "probing", "sensitive"]:
            escalation_score += 2
            flags.append("intent_escalation")

    # 2. Direct malicious follow-up
    # If user reaches malicious intent after probing/sensitive behavior
    if len(intents) >= 2:
        if intents[-1] == "malicious" and intents[-2] in ["probing", "sensitive"]:
            escalation_score += 2
            flags.append("malicious_followup")

    # 3. Repeated probing
    # Multiple probing attempts in one session
    if intents.count("probing") >= 3:
        escalation_score += 2
        flags.append("repeated_probing")

    # 4. Repeated sensitive attempts
    # Multiple sensitive requests suggest extraction behavior
    if intents.count("sensitive") >= 2:
        escalation_score += 2
        flags.append("repeated_sensitive_requests")

    # 5. Persistence after high-risk detection
    # If high risk appears more than once, attacker may be retrying
    if risks.count("high") >= 2:
        escalation_score += 3
        flags.append("persistent_high_risk_behavior")

    return escalation_score, flags