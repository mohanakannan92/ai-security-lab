import sys
import os

# Path to pattern weighting module
PATTERN_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../09-adaptive-learning")
)

# If pattern_weighting is inside another folder, adjust accordingly
# sys.path.append(PATTERN_DIR)

from pattern_weighting import pattern_weight_guard


def apply_guardrails(user_input):
    result = pattern_weight_guard(user_input)

    decision = result["action"]

    if decision == "block":
        return {
            "status": "blocked",
            "response": result["response"],
            "meta": result
        }

    elif decision == "guard":
        return {
            "status": "guarded",
            "response": result["response"],
            "meta": result
        }

    else:
        return {
            "status": "allowed",
            "response": None,
            "meta": result
        }