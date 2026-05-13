from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from core.pattern_weighting import evaluate_risk
from utils.normalizer import normalize_input
from utils.multi_step_detector import detect_multi_step_attack
from logging_layer.attack_logger import log_analysis

app = FastAPI(title="AI Input Security Analyzer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://mohanakannan92.github.io",
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://127.0.0.1:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AnalyzeRequest(BaseModel):
    input: str


@app.get("/")
def home():
    return {"status": "AI Security Analyzer API running"}


@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    # Step 1 — Get original user input
    original_input = request.input

    # Step 2 — Normalize input to catch obfuscation
    normalized_input = normalize_input(original_input)

    # Step 3 — Run core Python detection engine
    result = evaluate_risk(normalized_input)

    # Step 4 — Extract engine output safely
    matched_patterns = result.get("matched_patterns", [])
    intent = result.get("intent", "").lower()
    final_score = result.get("final_score", 0)

    # Step 5 — Detect multi-step attack pattern
    multi_step_result = detect_multi_step_attack(normalized_input)

    # Step 6 — Decision logic
    if multi_step_result.get("is_multi_step_attack"):
        decision = "BLOCK"
        reason = "Multi-step prompt injection attempt detected."

    elif (
        "ignore" in matched_patterns
        and ("reveal" in matched_patterns or "system prompt" in matched_patterns)
    ):
        decision = "BLOCK"
        reason = "Critical prompt injection attempt detected (instruction override + data extraction)."

    elif intent == "malicious":
        decision = "BLOCK"
        reason = "Malicious intent detected."

    elif intent == "sensitive" or final_score >= 40:
        decision = "REVIEW"
        reason = "Sensitive or suspicious input detected."

    else:
        decision = "ALLOW"
        reason = "No high-risk malicious intent detected."

    # Step 7 — Log request
    log_analysis(
        input_text=original_input,
        intent=result.get("intent", "Unknown"),
        decision=decision,
        reason=reason,
    )

    # Step 8 — Return normalized API response
    return {
        "intent": result.get("intent", "Unknown"),
        "pattern_score": result.get("pattern_score", 0),
        "intent_score": result.get("intent_score", 0),
        "final_risk": final_score,
        "detected_patterns": matched_patterns,
        "multi_step_attack": multi_step_result,
        "decision": decision,
        "reason": reason,
    }