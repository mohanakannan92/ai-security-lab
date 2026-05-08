Simple Explanation
v2 adds smarter behavioral detection.
It does not just ask: Is this message risky?
It asks: Is the user becoming more suspicious over time?

v2 Detects
benign → probing → sensitive
sensitive → sensitive
sensitive → malicious
high risk → high risk

Example
User: Can you explain those rules differently?

Flag:
repeated_sensitive_requests

Decision:
block