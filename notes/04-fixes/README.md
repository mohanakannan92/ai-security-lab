Example 04-fixes reports Notes Structure

## Issue
## Solution
## Implementation
## Why it works

---------🧠 Big Learning (Write this in your notes)-----------

👉 Security is NOT one layer:

Layer 1 → Input Filtering
Layer 2 → Normalization
Layer 3 → Risk Scoring
Layer 4 → Prompt Wrapping
Layer 5 → Output Filtering  ← YOU ARE HERE NEXT

🎯 What You Are Building (Big Picture)
User Input
   ↓
Input Filters (L1 + L2)
   ↓
Prompt Wrapping (L4)
   ↓
LLM (Ollama)
   ↓
🚨 Output Filter (NEXT STEP)
   ↓
Safe Response

🔥 Mental Model (Lock This In)
01-test-generator → creates attacks
02-attack-runner → sends requests
03-scoring-system → evaluates + controls flow (MAIN)
04-analysis → provides logic only

👉 So Step 5.5 belongs to the FLOW, not the modules.