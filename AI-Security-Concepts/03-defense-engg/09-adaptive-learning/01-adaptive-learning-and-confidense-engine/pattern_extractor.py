import re
from collections import Counter

STOPWORDS = {
    "what", "when", "where", "which", "your", "you", "are",
    "following", "about", "tell", "explain", "please", "can",
    "could", "would", "should", "this", "that", "with"
}


def extract_keywords(prompt):
    words = re.findall(r"\b[a-zA-Z]{4,}\b", prompt.lower())
    return [word for word in words if word not in STOPWORDS]


def build_pattern_frequency(logs):
    counter = Counter()

    for log in logs:
        if log["status"].lower() == "leak":
            keywords = extract_keywords(log["prompt"])
            counter.update(keywords)

    return counter