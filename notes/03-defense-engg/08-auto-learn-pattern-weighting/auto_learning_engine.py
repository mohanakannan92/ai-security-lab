import os
import pandas as pd
from collections import Counter
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "attack_logs.csv")

print("📂 CSV PATH:", CSV_PATH)

# 🚫 Stopwords (noise words)
STOPWORDS = {
    "what", "your", "this", "that", "with", "from", "have",
    "will", "about", "there", "their", "give", "tell"
}


# 🔍 Extract meaningful keywords
def extract_keywords(text):
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())

    # 🚀 Apply stopword filtering
    filtered = [w for w in words if w not in STOPWORDS]

    return filtered


# 🧠 Learn patterns from logs
def learn_patterns(min_freq=2):

    # 🧱 Cold start
    if not os.path.exists(CSV_PATH):
        print("ℹ️ No logs found — initializing CSV")
        with open(CSV_PATH, "w") as f:
            f.write("query,score,risk,action\n")
        return {}

    df = pd.read_csv(CSV_PATH)

    if df.empty:
        print("ℹ️ CSV exists but no data yet")
        return {}

    # 🎯 Focus only on risky queries
    attack_queries = df[df["action"].isin(["block", "guard"])]["query"]

    counter = Counter()

    for q in attack_queries:
        counter.update(extract_keywords(q))

    print("\n📊 Keyword Frequency:")
    for word, freq in counter.items():
        print(f"{word}: {freq}")

    # 🧠 Filter by frequency
    learned = {
        word: freq for word, freq in counter.items()
        if freq >= min_freq
    }

    print("\n🧠 Learned Patterns:")
    print(learned)

    return learned