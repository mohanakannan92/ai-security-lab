# attack_runner.py
import sys
import os
import requests

# Get current file location
current_dir = os.path.dirname(os.path.abspath(__file__))

# Go to sibling folder (01-test-generator)
generator_path = os.path.join(current_dir, "..", "01-test-generator")

# Add to Python path
sys.path.append(generator_path)

# Now import works
from attack_generator import generate_bulk_attacks

# Your API endpoint
API_URL = "http://127.0.0.1:8000/chat"

# Number of attacks to test
NUM_ATTACKS = 10


def run_attacks():
    # Step 1: Generate attacks
    attacks = generate_bulk_attacks(NUM_ATTACKS)

    results = []

    # Step 2: Loop through attacks
    for attack in attacks:
        prompt = attack["attack"]
        category = attack["category"]

        try:
            # Step 3: Send request to API
            response = requests.post(
                API_URL,
                params={"prompt": prompt}  # FastAPI expects query param
            )

            result = response.json()

        except Exception as e:
            result = {"error": str(e)}

        # Step 4: Store result
        results.append({
            "category": category,
            "attack": prompt,
            "result": result
        })

    return results


def print_results(results):
    # Step 5: Display results clearly
    for i, r in enumerate(results, 1):
        print("\n" + "="*50)
        print(f"Test #{i}")
        print(f"Category : {r['category']}")
        print(f"Attack   : {r['attack']}")
        print(f"Response : {r['result']}")


# Run directly
if __name__ == "__main__":
    results = run_attacks()
    print_results(results)