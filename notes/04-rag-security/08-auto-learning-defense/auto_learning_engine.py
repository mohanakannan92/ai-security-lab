import pandas as pd
import re
import os
from collections import Counter


# -------------------------------
# Normalize text
# -------------------------------
def normalize(text):
    text = re.sub(r"[^\w\s]", "", text.lower())
    return text.strip()


# -------------------------------
# Extract meaningful keywords
# -------------------------------
def extract_keywords(query):
    words = query.split()
    return [w for w in words if len(w) > 4]


# -------------------------------
# Learning Engine
# -------------------------------
def learn_from_logs(csv_path):
    if not os.path.exists(csv_path):
        print(f"❌ CSV not found at: {csv_path}")
        return []

    df = pd.read_csv(csv_path)

    if df.empty:
        print("⚠️ CSV is empty")
        return []

    # Focus on risky queries only
    risky_df = df[df["action"].isin(["guard", "block"])]

    all_keywords = []

    for q in risky_df["query"]:
        q = normalize(q)
        words = extract_keywords(q)
        all_keywords.extend(words)

    # Count frequency
    keyword_counts = Counter(all_keywords)

    STOPWORDS = {"level", "guide", "answers", "responses", "what", "give"}

    # 🔥 IMPORTANT: low threshold for early learning
    learned_patterns = [
    word for word, count in keyword_counts.items()
    if count >= 2 and word not in STOPWORDS
    ]

    # -------------------------------
    # Debug Output
    # -------------------------------
    print("\n📊 Keyword Frequency:")
    for k, v in keyword_counts.items():
        print(f"{k}: {v}")

    print("\n🧠 Learned Patterns:")
    print(learned_patterns)

    return learned_patterns


# -------------------------------
# Entry Point (VERY IMPORTANT)
# -------------------------------
if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Adjust path based on your structure
    CSV_PATH = os.path.join(BASE_DIR, "attack_logs.csv")

    print("📂 Looking for CSV at:")
    print(CSV_PATH)

    patterns = learn_from_logs(CSV_PATH)