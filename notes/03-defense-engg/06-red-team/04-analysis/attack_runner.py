# attack_runner.py

import sys
import os
import requests

# -------------------------------
# Fix paths FIRST (before import)
# -------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))

generator_path = os.path.join(current_dir, "..", "01-test-generator")
sys.path.append(generator_path)

evaluator_path = os.path.join(current_dir, "..", "03-scoring-system")
sys.path.append(evaluator_path)

analysis_path = os.path.join(current_dir, "..", "04-analysis")
sys.path.append(analysis_path)

# -------------------------------
# Imports
# -------------------------------
from attack_generator import generate_bulk_attacks
from evaluator import evaluate_response

from analyzer import analyze_results, calculate_metrics, detect_weakness
from report import generate_report

# -------------------------------
# Config
# -------------------------------
API_URL = "http://127.0.0.1:8000/chat"
NUM_ATTACKS = 10


def run_attacks():
    attacks = generate_bulk_attacks(NUM_ATTACKS)
    print("Generated attacks:", attacks)

    detailed_results = []
    analysis_input = []

    for attack in attacks:
        prompt = attack.get("attack")
        category = attack.get("category")

        try:
            response = requests.post(
                API_URL,
                params={"prompt": prompt},
                timeout=10
            )

            # Handle non-JSON safely
            try:
                result = response.json()
            except Exception:
                result = {"error": "Invalid JSON response", "raw": response.text}

        except Exception as e:
            result = {"error": str(e)}

        # -------------------------------
        # Evaluate response
        # -------------------------------
        evaluation = evaluate_response(result)

        # -------------------------------
        # Normalize status (CORRECT LOGIC)
        # -------------------------------
        if evaluation.get("leak") is True:
            status = "leak"
        elif evaluation.get("blocked") is True:
            status = "blocked"
        else:
            status = "bypass"

        # -------------------------------
        # Store detailed results
        # -------------------------------
        detailed_results.append({
            "category": category,
            "attack": prompt,
            "result": result,
            "evaluation": evaluation,
            "status": status  # useful for debugging
        })

        # -------------------------------
        # Store minimal analysis input
        # -------------------------------
        analysis_input.append({
            "attack_type": category,
            "status": status
        })

    return detailed_results, analysis_input


def print_results(results):
    for i, r in enumerate(results, 1):
        print("\n" + "=" * 50)
        print(f"Test #{i}")
        print(f"Category   : {r['category']}")
        print(f"Attack     : {r['attack']}")
        print(f"Response   : {r['result']}")
        print(f"Evaluation : {r['evaluation']}")
        print(f"Status     : {r['status']}")


# -------------------------------
# MAIN EXECUTION
# -------------------------------
if __name__ == "__main__":
    detailed_results, analysis_input = run_attacks()

    print("\nTotal results:", len(detailed_results))
    print_results(detailed_results)

    # -------------------------------
    # ✅ Step 5 — Analysis Layer (RUN ONCE)
    # -------------------------------
    summary = analyze_results(analysis_input)
    metrics = calculate_metrics(summary)
    weaknesses = detect_weakness(summary)

    generate_report(summary, metrics, weaknesses)