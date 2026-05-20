import re
from collections import Counter
from adaptive_learning.log_parser import read_attack_logs
from pathlib import Path


STOPWORDS = {
    "the", "is", "are", "a", "an", "to", "of", "and", "or", "in",
    "on", "for", "with", "me", "you", "your", "my", "i", "it",
    "this", "that", "please", "explain", "tell", "show",
    "first", "say", "hello", "then", "all"
}


def extract_keywords_from_logs(logs):
    """
    Extracts repeated meaningful words from logged user inputs.

    Purpose:
    - Read the 'input' field from each log row
    - Normalize text
    - Remove common words
    - Count important repeated words
    """

    all_words = []

    for log in logs:
        user_input = log.get("input", "")

        normalized = user_input.lower()

        words = re.findall(r"\b[a-zA-Z]+\b", normalized)

        meaningful_words = [
            word for word in words
            if word not in STOPWORDS and len(word) > 2
        ]

        all_words.extend(meaningful_words)

    return Counter(all_words)


def display_keywords(keyword_counts, top_n=10):
    """
    Displays top repeated keywords.
    """

    print("\n=== Learned Keyword Frequency ===")

    if not keyword_counts:
        print("No keywords found.")
        return

    for word, count in keyword_counts.most_common(top_n):
        print(f"{word}: {count}")


if __name__ == "__main__":

    BASE_DIR = Path(__file__).resolve().parent
    LOG_FILE = BASE_DIR.parent / "logging_layer" / "attack_logs.csv"

    logs = read_attack_logs(LOG_FILE)

    keyword_counts = extract_keywords_from_logs(logs)

    display_keywords(keyword_counts)