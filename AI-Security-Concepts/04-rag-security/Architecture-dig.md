🧱 Layer-wise Visibility Model
1️⃣ RAG Defense Layer (03-rag_smart_defense)

Track:

Docs retrieved
Docs removed (malicious)
Docs sanitized
Injection attempts inside context
2️⃣ Semantic Layer (04/05)

Track:

Intent detected
Sensitive queries
False positives / negatives
3️⃣ Confidence Layer (06-confidence-defense)

Track:

Score
Risk level
Final decision
🧠 Final Architecture (What you’re building toward)


                ┌────────────────────┐
Query ────────► │  RAG Defense Layer │
                └────────┬───────────┘
                         │
                         ▼
                ┌────────────────────┐
                │ Semantic Detection │
                └────────┬───────────┘
                         │
                         ▼
                ┌────────────────────┐
                │ Confidence Scoring │
                └────────┬───────────┘
                         │
                         ▼
                ┌────────────────────┐
                │   Final Decision   │
                └────────┬───────────┘
                         │
                         ▼
                📊 Unified Dashboard