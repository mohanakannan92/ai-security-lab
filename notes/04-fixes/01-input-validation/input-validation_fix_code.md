from fastapi import FastAPI
import ollama

app = FastAPI()

def is_malicious(input_text: str):
    blocked_patterns = [
        "ignore previous instructions",
        "reveal system prompt",
        "you are now system",
        "repeat everything",
        "### system"
    ]
    
    for pattern in blocked_patterns:
        if pattern.lower() in input_text.lower():
            return True
    return False


@app.post("/chat")
def chat(prompt: str):
    
    if is_malicious(prompt):
        return {"error": "Malicious input detected"}

    response = ollama.generate(
        model="tinyllama",
        prompt=prompt
    )

    return response