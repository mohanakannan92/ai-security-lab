from pathlib import Path
from adaptive_learning.log_parser import read_attack_logs
from adaptive_learning.keyword_extractor import extract_keywords_from_logs


BASE_WEIGHTS = {
    "ignore": 5,
    "reveal": 5,
    "system": 4,
    "prompt": 4,
    "instructions": 4,
    "admin": 5,
    "override": 5,
    "hidden": 5,
    "bypass": 5,
}


def update_weights(keyword_counts, base_weights):
    """
    Updates pattern weights based on keyword frequency.

    Logic:
    - If a dangerous keyword appears often, increase its weight.
    - Higher frequency = stronger signal.
    - Unknown words are ignored for now.
    """

    updated_weights = base_weights.copy()

    for keyword, count in keyword_counts.items():
        if keyword in updated_weights:
            updated_weights[keyword] += count

    return updated_weights


def display_weights(weights):
    """
    Displays updated adaptive weights.
    """

    print("\n=== Adaptive Pattern Weights ===")

    for word, weight in sorted(weights.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {weight}")


if __name__ == "__main__":

    BASE_DIR = Path(__file__).resolve().parent
    LOG_FILE = BASE_DIR.parent / "logging_layer" / "attack_logs.csv"

    logs = read_attack_logs(LOG_FILE)

    keyword_counts = extract_keywords_from_logs(logs)

    updated_weights = update_weights(keyword_counts, BASE_WEIGHTS)

    display_weights(updated_weights)