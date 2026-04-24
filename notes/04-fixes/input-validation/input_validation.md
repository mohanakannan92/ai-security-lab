# Input Validation Fix

## Issue
The API accepts user input directly and sends it to the LLM without validation.

This allows attackers to:
- Override system behavior
- Inject malicious instructions
- Attempt data extraction

Example attacks:
- "Ignore previous instructions"
- "Reveal system prompt"
- "Repeat everything"

---

## Solution
Introduce an input validation layer to detect and block malicious patterns before sending data to the LLM.

This acts as a basic security filter between user and model.

---

## Implementation

```python
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

Why it works
Blocks known malicious patterns before reaching the model
Prevents simple prompt injection attempts
Adds a security layer between user and LLM

However:

This is a basic rule-based approach
Can be bypassed using obfuscation or variations
Needs more advanced techniques for real-world security