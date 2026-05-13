from feedback_analyzer import analyze_feedback
import sys
import os

# add path for threshold module
THRESHOLD_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../02-auto-threshold-tuning")
)

sys.path.append(THRESHOLD_DIR)

from threshold_tuner import tune_thresholds


def run_feedback_tuning():
    result = analyze_feedback()

    false_positive_count = result["false_positive_count"]
    false_negative_count = result["false_negative_count"]

    print("🔍 Feedback Summary:", result)

    updated_config = tune_thresholds(
        leak_count=false_negative_count,
        false_positive_count=false_positive_count
    )

    print("\n⚙️ Updated Thresholds:", updated_config)
    print("Path:", THRESHOLD_DIR)
    print("Exists:", os.path.exists(THRESHOLD_DIR))

if __name__ == "__main__":
    run_feedback_tuning()