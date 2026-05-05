import os
import pandas as pd
import streamlit as st

st.set_page_config(page_title="AI Security Dashboard", layout="wide")

st.title("🛡️ AI Security Dashboard")

# ✅ FIXED PATH
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR,"attack_logs.csv")

if not os.path.exists(LOG_PATH):
    st.error("❌ attack_logs.csv not found. Run test scripts first.")
    st.stop()

df = pd.read_csv(LOG_PATH)

st.subheader("📊 Metrics")
st.write("Total:", len(df))

# -------------------------------
# Basic Metrics
# -------------------------------
st.subheader("📊 Metrics")

st.write("Total Requests:", len(df))
st.write("Blocked:", len(df[df["action"] == "block"]))
st.write("Guarded:", len(df[df["action"] == "guard"]))
st.write("Allowed:", len(df[df["action"] == "allow"]))

# -------------------------------
# RAG Insights
# -------------------------------
st.subheader("📚 RAG Pipeline Insights")

st.line_chart(df[["retrieved_docs", "sanitized_docs"]])

# -------------------------------
# Risk Distribution
# -------------------------------
st.subheader("📊 Risk Distribution")

st.bar_chart(df["risk"].value_counts())

# -------------------------------
# Semantic Flags
# -------------------------------
st.subheader("🧠 Semantic Detection")

st.bar_chart(df["semantic_flag"].value_counts())

# -------------------------------
# Recent Logs
# -------------------------------
st.subheader("📋 Recent Activity")

st.dataframe(df.tail(10))