# attack_runner.py

import sys
import os
import requests

# -------------------------------
# Fix paths FIRST (before import)
# -------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))

# Generator path
generator_path = os.path.join(current_dir, "..", "01-test-generator")
sys.path.append(generator_path)

# Evaluator path
evaluator_path = os.path.join(current_dir, "..", "03-scoring-system")
sys.path.append(evaluator_path)

# -------------------------------
# Now import modules
# -------------------------------
from attack_generator import generate_bulk_attacks
from evaluator import evaluate_response

# -------------------------------
# API endpoint
# -------------------------------
API_URL = "http://127.0.0.1:8000/chat"

# Number of attacks
NUM_ATTACKS = 10


def run_attacks():
    # Generate attacks
    attacks = generate_bulk_attacks(NUM_ATTACKS)
    print("Generated attacks:", attacks)

    results = []

    for attack in attacks:
        prompt = attack["attack"]
        category = attack["category"]

        try:
            # Send request to API
            response = requests.post(
                API_URL,
                params={"prompt": prompt}
            )

            result = response.json()

        except Exception as e:
            result = {"error": str(e)}

        # -------------------------------
        # Evaluate response (NEW)
        # -------------------------------
        evaluation = evaluate_response(result)

        # Store everything
        results.append({
            "category": category,
            "attack": prompt,
            "result": result,
            "evaluation": evaluation
        })

    return results


def print_results(results):
    for i, r in enumerate(results, 1):
        print("\n" + "=" * 50)
        print(f"Test #{i}")
        print(f"Category   : {r['category']}")
        print(f"Attack     : {r['attack']}")
        print(f"Response   : {r['result']}")
        print(f"Evaluation : {r['evaluation']}")


# Run script
if __name__ == "__main__":
    results = run_attacks()
    print("Total results:", len(results))
    print_results(results)