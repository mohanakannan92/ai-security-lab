import csv
import os

# File will ALWAYS be created in: 09-adaptive-learning/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "attack_logs.csv")

def log_attack(prompt, category, status):
    file_exists = os.path.isfile(FILE_PATH)

    with open(FILE_PATH, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["prompt", "category", "status"])

        writer.writerow([prompt, category, status])