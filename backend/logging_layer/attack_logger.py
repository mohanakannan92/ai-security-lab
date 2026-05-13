import csv
from datetime import datetime
from pathlib import Path

LOG_FILE = Path(__file__).parent / "attack_logs.csv"

def log_analysis(input_text: str, intent: str, decision: str, reason: str) -> None:
    file_exists = LOG_FILE.exists()
    print("LOGGING CALLED")

    with open(LOG_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "input",
                "intent",
                "decision",
                "reason"
            ])

        writer.writerow([
            datetime.now().isoformat(),
            input_text,
            intent,
            decision,
            reason
        ])