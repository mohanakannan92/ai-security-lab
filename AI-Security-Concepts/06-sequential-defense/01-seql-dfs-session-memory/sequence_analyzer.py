def analyze_sequence(session):
    intents = session["intents"]
    risks = session["risks"]

    escalation_score = 0
    flags = []

    # 🔥 Escalation pattern
    if len(intents) >= 3:
        if intents[-3:] == ["benign", "probing", "sensitive"]:
            escalation_score += 2
            flags.append("intent_escalation")

    # 🔥 Repeated probing
    if intents.count("probing") >= 3:
        escalation_score += 2
        flags.append("repeated_probing")

    # 🔥 Persistence after refusal
    if risks.count("high") >= 2:
        escalation_score += 3
        flags.append("persistent_attack")

    return escalation_score, flags