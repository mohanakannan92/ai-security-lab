import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FEEDBACK_PATH = os.path.join(BASE_DIR, "feedback_logs.csv")


def log_feedback(prompt, expected_status, actual_action):
    """
    expected_status:
        - attack
        - benign

    actual_action:
        - block
        - guard
        - allow
    """

    file_exists = os.path.isfile(FEEDBACK_PATH)

    with open(FEEDBACK_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "prompt",
                "expected_status",
                "actual_action",
                "feedback_type"
            ])

        feedback_type = classify_feedback(expected_status, actual_action)

        writer.writerow([
            prompt,
            expected_status,
            actual_action,
            feedback_type
        ])


def classify_feedback(expected_status, actual_action):
    if expected_status == "attack" and actual_action == "allow":
        return "false_negative"

    if expected_status == "benign" and actual_action in ["block", "guard"]:
        return "false_positive"

    return "correct"