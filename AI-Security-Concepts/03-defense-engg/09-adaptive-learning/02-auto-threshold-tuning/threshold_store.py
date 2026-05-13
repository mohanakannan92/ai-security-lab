import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "threshold_config.json")


def load_thresholds():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_thresholds(config):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)