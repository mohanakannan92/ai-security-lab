from pathlib import Path

from adaptive_learning.log_parser import read_attack_logs
from adaptive_learning.keyword_extractor import extract_keywords_from_logs
from adaptive_learning.weight_updater import BASE_WEIGHTS, update_weights


def build_adaptive_weights(log_file_path=None):
    """
    Main adaptive learning function.

    Purpose:
    - Read attack history from attack_logs.csv
    - Extract repeated security-relevant keywords
    - Update pattern weights dynamically
    - Return adaptive weights to other modules

    This function becomes the reusable interface for adaptive learning.
    """

    if log_file_path is None:
        base_dir = Path(__file__).resolve().parent
        log_file_path = base_dir.parent / "logging_layer" / "attack_logs.csv"

    logs = read_attack_logs(log_file_path)

    if not logs:
        return BASE_WEIGHTS.copy()

    keyword_counts = extract_keywords_from_logs(logs)

    adaptive_weights = update_weights(keyword_counts, BASE_WEIGHTS)

    return adaptive_weights


def display_adaptive_engine_summary(adaptive_weights):
    """
    Prints adaptive engine output for testing and debugging.
    """

    print("\n=== Adaptive Engine Summary ===")
    print("Generated adaptive weights:\n")

    for word, weight in sorted(adaptive_weights.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {weight}")


if __name__ == "__main__":
    adaptive_weights = build_adaptive_weights()
    display_adaptive_engine_summary(adaptive_weights)