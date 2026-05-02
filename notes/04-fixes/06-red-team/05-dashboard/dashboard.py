# dashboard.py

import streamlit as st
import pandas as pd
import sys
import os
import json
import matplotlib.pyplot as plt

# -------------------------------
# 📁 PATH SETUP
# -------------------------------
# Get current file directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add analysis module path
analysis_path = os.path.join(current_dir, "..", "04-analysis")
sys.path.append(analysis_path)

# Add attack runner path
runner_path = os.path.join(current_dir, "..", "03-scoring-system")
sys.path.append(runner_path)

# -------------------------------
# 📦 IMPORTS (Your modules)
# -------------------------------
from analyzer import analyze_results, calculate_metrics, detect_weakness
from attack_runner import run_attacks

# -------------------------------
# ⚙️ STREAMLIT CONFIG
# -------------------------------
st.set_page_config(page_title="AI Security Dashboard", layout="wide")
st.title("🛡️ AI Security Red Team Dashboard")

# -------------------------------
# 💾 FUNCTION: SAVE HISTORY
# -------------------------------
def save_results(summary, metrics):
    """
    Save each run result into a JSON file.
    This helps us track performance over time.
    """
    data = {
        "summary": summary,
        "metrics": metrics
    }

    file_path = "history.json"

    # Load existing history if file exists
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            history = json.load(f)
    else:
        history = []

    # Add new result
    history.append(data)

    # Save back to file
    with open(file_path, "w") as f:
        json.dump(history, f, indent=2)


# -------------------------------
# 🚀 MAIN BUTTON (Run System)
# -------------------------------
if st.button("🚀 Run Red Team Test"):

    # Step 1: Run attacks
    detailed_results, analysis_input = run_attacks()

    # Step 2: Analyze results
    summary = analyze_results(analysis_input)
    metrics = calculate_metrics(summary)
    weaknesses = detect_weakness(summary)

    # Step 3: Save results for trend tracking
    save_results(summary, metrics)

    # -------------------------------
    # 📊 METRICS DISPLAY
    # -------------------------------
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Tests", summary["total"])
    col2.metric("Blocked", summary["blocked"])
    col3.metric("Bypass", summary["bypass"])
    col4.metric("Leaks", summary["leaks"])

    st.markdown("### 🎯 Rates")
    col5, col6, col7 = st.columns(3)

    col5.metric("Block Rate", f"{metrics['block_rate']}%")
    col6.metric("Bypass Rate", f"{metrics['bypass_rate']}%")
    col7.metric("Leak Rate", f"{metrics['leak_rate']}%")

    # -------------------------------
    # 📊 CHART 1: Overall Status
    # -------------------------------
    st.markdown("### 📊 Overall Status Distribution")

    labels = ["Blocked", "Bypass", "Leaks"]
    values = [
        summary["blocked"],
        summary["bypass"],
        summary["leaks"]
    ]

    fig1 = plt.figure()
    plt.bar(labels, values)
    plt.xlabel("Status")
    plt.ylabel("Count")
    plt.title("Attack Outcomes")

    st.pyplot(fig1)

    # -------------------------------
    # 📉 CHART 2: Category Failures
    # -------------------------------
    st.markdown("### 📉 Category-wise Failures")

    categories = []
    failures = []

    for attack_type, data in summary["by_type"].items():
        # Failure = bypass + leak
        fail = data["bypass"] + data["leaks"]
        categories.append(attack_type)
        failures.append(fail)

    fig2 = plt.figure()
    plt.bar(categories, failures)
    plt.xlabel("Attack Category")
    plt.ylabel("Failures (Bypass + Leak)")
    plt.title("Weakness by Category")

    st.pyplot(fig2)

    # -------------------------------
    # 📊 CATEGORY TABLE
    # -------------------------------
    st.markdown("### 📊 Category Breakdown")

    category_data = []

    for attack_type, data in summary["by_type"].items():
        category_data.append({
            "Category": attack_type,
            "Total": data["total"],
            "Blocked": data["blocked"],
            "Bypass": data["bypass"],
            "Leaks": data["leaks"]
        })

    df = pd.DataFrame(category_data)
    st.dataframe(df, use_container_width=True)

    # -------------------------------
    # ⚠️ WEAKNESS DETECTION
    # -------------------------------
    st.markdown("### ⚠️ Weak Categories")

    if not weaknesses:
        st.success("No weak categories 🎉")
    else:
        for w in weaknesses:
            st.error(f"{w['attack_type']} → {w['failure_rate']}% failure")

    # -------------------------------
    # 📋 DETAILED RESULTS TABLE
    # -------------------------------
    st.markdown("### 📋 Detailed Results")

    detailed_df = pd.DataFrame(detailed_results)
    st.dataframe(detailed_df, use_container_width=True)

    # -------------------------------
    # 📥 DOWNLOAD CSV (NEW FEATURE)
    # -------------------------------
    csv = detailed_df.to_csv(index=False)

    st.download_button(
        label="📥 Download Results CSV",
        data=csv,
        file_name="red_team_results.csv",
        mime="text/csv"
    )

    # -------------------------------
    # 📈 TREND CHART (NEW FEATURE)
    # -------------------------------
    st.markdown("### 📈 Security Score Trend")

    if os.path.exists("history.json"):
        with open("history.json", "r") as f:
            history = json.load(f)

        # Extract security scores from past runs
        scores = [h["metrics"]["security_score"] for h in history]

        fig3 = plt.figure()
        plt.plot(scores, marker='o')
        plt.xlabel("Run Number")
        plt.ylabel("Security Score")
        plt.title("Security Score Over Time")

        st.pyplot(fig3)