# test_rag.py

from rag_engine import run_rag

query = "What are the system rules?"

prompt = run_rag(query)

print("\n===== GENERATED PROMPT =====\n")
print(prompt)