import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "pattern_store.json")


def load_patterns():
    if not os.path.exists(FILE_PATH):
        return {}

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_patterns(patterns):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(patterns, f, indent=2)