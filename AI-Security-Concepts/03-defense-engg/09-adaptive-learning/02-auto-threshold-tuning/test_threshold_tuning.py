from threshold_tuner import tune_thresholds
from threshold_store import load_thresholds

print("Before tuning:")
print(load_thresholds())

print("\nCase 1: Too many leaks")
updated = tune_thresholds(leak_count=4, false_positive_count=0)
print(updated)

print("\nCase 2: Too many false positives")
updated = tune_thresholds(leak_count=0, false_positive_count=4)
print(updated)

print("\nCase 3: Balanced system")
updated = tune_thresholds(leak_count=1, false_positive_count=1)
print(updated)