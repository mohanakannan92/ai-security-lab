import csv
import os
from datetime import datetime

LOG_FILE = "attack_logs.csv"


def log_attack(query, decision, stage_data):
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "query",

                # Confidence layer
                "risk",
                "score",
                "action",
                "matches",

                # RAG layer
                "retrieved_docs",
                "sanitized_docs",
                "malicious_detected",

                # Semantic layer
                "semantic_flag"
            ])

        writer.writerow([
            datetime.now(),
            query,

            decision["risk"],
            decision["score"],
            decision["action"],
            ", ".join(decision["matches"]),

            stage_data.get("retrieved_docs", 0),
            stage_data.get("sanitized_docs", 0),
            stage_data.get("malicious_detected", False),

            stage_data.get("semantic_flag", False)
        ])