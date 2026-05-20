import csv
from pathlib import Path


def read_attack_logs(log_file_path):
    """
    Reads attack_logs.csv and returns log entries as a list of dictionaries.

    Why this exists:
    - The logging layer records what users entered
    - Adaptive learning needs those historical inputs
    - This parser converts CSV rows into Python-readable data
    """

    log_path = Path(log_file_path)

    if not log_path.exists():
        print(f"[ERROR] Log file not found: {log_file_path}")
        return []

    logs = []

    with open(log_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            logs.append(row)

    return logs


def display_log_summary(logs):
    """
    Prints a simple summary of parsed logs.
    This helps us verify that CSV reading is working.
    """

    print("\n=== Attack Log Summary ===")
    print(f"Total log entries found: {len(logs)}")

    if logs:
        print("\nSample log entry:")
        print(logs[0])


if __name__ == "__main__":

    # Get current file location safely
    BASE_DIR = Path(__file__).resolve().parent

    # Build absolute path to attack_logs.csv
    LOG_FILE = BASE_DIR.parent / "logging_layer" / "attack_logs.csv"

    logs = read_attack_logs(LOG_FILE)
    display_log_summary(logs)