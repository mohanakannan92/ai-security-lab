from log_loader import load_logs
from pattern_extractor import build_pattern_frequency
from pattern_updater import update_pattern_weights
from pattern_store import load_patterns, save_patterns
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "attack_logs.csv")

logs = load_logs(CSV_PATH)

pattern_freq = build_pattern_frequency(logs)

existing = load_patterns()

updated = update_pattern_weights(pattern_freq, existing)

save_patterns(updated)

print("✅ Learning completed")
print(updated)