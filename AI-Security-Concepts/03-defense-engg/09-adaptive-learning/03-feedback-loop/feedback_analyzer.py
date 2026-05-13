import csv
import os
from collections import Counter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FEEDBACK_PATH = os.path.join(BASE_DIR, "feedback_logs.csv")


def analyze_feedback():
    if not os.path.exists(FEEDBACK_PATH):
        return {
            "false_positive_count": 0,
            "false_negative_count": 0,
            "correct_count": 0,
            "total": 0
        }

    counter = Counter()

    with open(FEEDBACK_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            counter[row["feedback_type"]] += 1

    total = sum(counter.values())

    return {
        "false_positive_count": counter["false_positive"],
        "false_negative_count": counter["false_negative"],
        "correct_count": counter["correct"],
        "total": total
    }