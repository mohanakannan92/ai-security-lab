import re


# -------------------------------
# 🚨 Dangerous Output Patterns
# -------------------------------
SENSITIVE_PATTERNS = [
    r"system prompt",
    r"internal instructions",
    r"developer message",
    r"hidden rules",
    r"confidential",
    r"override security",
]


# -------------------------------
# 🧠 Detect Sensitive Output
# -------------------------------
def detect_sensitive_output(text):
    text = text.lower()

    for pattern in SENSITIVE_PATTERNS:
        if re.search(pattern, text):
            return True, pattern

    return False, None


# -------------------------------
# 🧼 Sanitize Output
# -------------------------------
def sanitize_output(text):
    is_sensitive, pattern = detect_sensitive_output(text)

    if is_sensitive:
        return {
            "status": "blocked",
            "reason": f"Sensitive pattern detected: {pattern}",
            "safe_response": "I cannot provide that information."
        }

    return {
        "status": "clean",
        "response": text
    }