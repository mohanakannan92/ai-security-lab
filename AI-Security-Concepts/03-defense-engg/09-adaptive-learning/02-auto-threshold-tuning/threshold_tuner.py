from threshold_store import load_thresholds, save_thresholds


def tune_thresholds(leak_count, false_positive_count):
    config = load_thresholds()

    high_threshold = config["high_threshold"]
    medium_threshold = config["medium_threshold"]

    # If leaks are high, system is too loose → lower thresholds
    if leak_count >= 3:
        high_threshold -= 1
        medium_threshold -= 1

    # If false positives are high, system is too strict → raise thresholds
    if false_positive_count >= 3:
        high_threshold += 1
        medium_threshold += 1

    # Keep thresholds inside safe limits
    high_threshold = max(config["min_high_threshold"], min(high_threshold, config["max_high_threshold"]))
    medium_threshold = max(config["min_medium_threshold"], min(medium_threshold, config["max_medium_threshold"]))

    config["high_threshold"] = high_threshold
    config["medium_threshold"] = medium_threshold

    save_thresholds(config)

    return config