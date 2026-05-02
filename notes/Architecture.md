🧠 AI Security Red Team System — Architecture
🔷 High-Level Flow
        ┌────────────────────────────┐
        │     Attack Generator       │
        │ (prompt_injection, etc.)   │
        └────────────┬───────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │      Attack Runner         │
        │  (API Requests Sender)     │
        └────────────┬───────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │   AI Security System API   │
        │  (Your Defense Pipeline)   │
        └────────────┬───────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │     Evaluation Engine      │
        │ (blocked / bypass / leak)  │
        └────────────┬───────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │   Analysis & Metrics Layer │
        │ (rates, weaknesses)        │
        └────────────┬───────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │   Visualization Dashboard  │
        │ (Streamlit UI + Charts)    │
        └────────────────────────────┘

🔍 Deep Architecture (Interview-Level)

🔐 1. Defense Pipeline (Inside API)
User Prompt
    │
    ▼
[ Input Filter Layer ]
    - basic keyword block
    - advanced pattern detection
    │
    ▼
[ Intent Detection Layer ]
    - meta query detection
    - policy extraction detection
    │
    ▼
[ Prompt Wrapping Layer ]
    - secure system prompt
    - instruction isolation
    │
    ▼
[ LLM Model ]
    │
    ▼
[ Output Filter Layer ]
    - leakage detection
    - response sanitization
    │
    ▼

Final Response

⚔️ 2. Red Team Engine
Attack Generator
    │
    ├── prompt_injection
    ├── role_override
    ├── instruction_bypass
    ├── multi_step
    ├── obfuscation
    └── data_extraction
    │
    ▼
Attack Runner
    │
    ├── Sends API requests
    ├── Handles timeout/errors
    └── Collects responses

📊 3. Evaluation + Analysis

API Response
    │
    ▼
Evaluation Engine
    │
    ├── blocked? (filter triggered)
    ├── leak? (sensitive output)
    └── bypass? (passed but safe reply)
    │
    ▼
Analyzer
    │
    ├── total / blocked / bypass / leaks
    ├── per-category stats
    └── weakness detection

📈 4. Dashboard Layer

Analysis Output
    │
    ▼
Streamlit Dashboard
    │
    ├── Metrics Cards
    ├── Charts (bar + trend)
    ├── Weakness Alerts
    ├── Detailed Table
    ├── CSV Export
    └── History Tracking (JSON)
🔥 Final One-Line Architecture (VERY IMPORTANT)

Use this in interviews:

“The system integrates a red team attack generator with a multi-layer AI defense pipeline, followed by automated evaluation, weakness analysis, and a real-time dashboard for security visibility.”

🎯 What Makes This Architecture Strong
✅ End-to-end pipeline (attack → defense → analysis → UI)
✅ Layered defense model (not single filter)
✅ Automated red teaming (rare in beginner projects)
✅ Observability (dashboard + metrics)