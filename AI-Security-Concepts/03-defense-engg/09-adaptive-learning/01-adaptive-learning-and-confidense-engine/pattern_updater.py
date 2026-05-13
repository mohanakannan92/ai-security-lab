MAX_WEIGHT = 10

def update_pattern_weights(pattern_freq, existing_patterns):
    for keyword, count in pattern_freq.items():
        current = existing_patterns.get(keyword, 0)
        existing_patterns[keyword] = min(current + count, MAX_WEIGHT)

    return existing_patterns