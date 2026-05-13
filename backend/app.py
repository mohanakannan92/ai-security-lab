from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pattern_weighting import evaluate_risk

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
    user_input = request.input

    result = evaluate_risk(user_input)

    risk_level = result.get("risk_level", "LOW")
    final_score = result.get("final_score", 0)

    if risk_level == "HIGH" or final_score >= 80:
        decision = "BLOCK"
        reason = "High-risk prompt injection, role override, or sensitive data extraction attempt detected."
    elif risk_level == "MEDIUM" or final_score >= 40:
        decision = "REVIEW"
        reason = "Suspicious AI security pattern detected. Manual validation is recommended."
    else:
        decision = "ALLOW"
        reason = "No high-risk malicious intent detected."

    return {
        "intent": result.get("intent", "Unknown"),
        "pattern_score": result.get("pattern_score", 0),
        "intent_score": result.get("intent_score", 0),
        "final_risk": final_score,
        "detected_patterns": result.get("matched_patterns", []),
        "decision": decision,
        "reason": reason
    }