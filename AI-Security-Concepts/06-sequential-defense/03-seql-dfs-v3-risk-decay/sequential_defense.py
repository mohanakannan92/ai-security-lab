from session_manager import SessionManager
from sequence_analyzer import analyze_sequence

session_manager = SessionManager()

RISK_SCORE = {
    "low": 1,
    "medium": 3,
    "high": 5
}

def apply_sequential_defense(user_id, message, intent, risk):
    session = session_manager.update_session(
        user_id, message, intent, risk
    )

    escalation_score, flags = analyze_sequence(session)

    # Convert risk label into numeric score
    base_risk_score = RISK_SCORE.get(risk.lower(), 1)

    final_risk_score = base_risk_score + escalation_score

    if final_risk_score >= 5:
        decision = "block"
    elif final_risk_score >= 3:
        decision = "warn"
    else:
        decision = "allow"

    return {
        "base_risk": risk,
        "base_risk_score": base_risk_score,
        "escalation_score": escalation_score,
        "final_risk_score": final_risk_score,
        "decision": decision,
        "flags": flags
    }