# rag_engine.py

import os

# -------------------------------
# Get base directory (IMPORTANT FIX)
# -------------------------------
# This ensures file paths work no matter where you run the script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# -------------------------------
# Load documents
# -------------------------------
def load_documents(file_path):
    """
    Reads document file and splits into chunks (basic approach)
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split documents by empty line
    docs = content.split("\n\n")

    return docs


# -------------------------------
# Simple keyword-based retrieval
# -------------------------------
def retrieve_docs(query, docs, top_k=2):
    """
    Very simple scoring:
    counts how many query words appear in document
    """
    scores = []

    for doc in docs:
        score = 0

        for word in query.lower().split():
            if word in doc.lower():
                score += 1

        scores.append((doc, score))

    # Sort documents by score (highest first)
    scores.sort(key=lambda x: x[1], reverse=True)

    # Return only top_k documents
    return [doc for doc, _ in scores[:top_k]]


# -------------------------------
# Build prompt with context
# -------------------------------
def build_prompt(query, context_docs):
    """
    Combines retrieved documents into a prompt
    """
    context = "\n".join(context_docs)

    prompt = f"""
You are a secure AI assistant.

Use the following context to answer:

{context}

User Question:
{query}

Answer:
"""
    return prompt


# -------------------------------
# Main RAG pipeline
# -------------------------------
def run_rag(query):
    """
    Full pipeline:
    Load → Retrieve → Build Prompt
    """

    # Build correct absolute path
    docs_path = os.path.join(BASE_DIR, "data", "docs.txt")

    # Load documents
    docs = load_documents(docs_path)

    # Retrieve relevant docs
    context_docs = retrieve_docs(query, docs)

    # Build final prompt
    prompt = build_prompt(query, context_docs)

    return prompt