# API Flow (User → FastAPI → LLM → Response)

## Flow

User → FastAPI → Ollama (LLM) → FastAPI → User

---

## What happens step-by-step

1. User sends prompt
2. FastAPI receives request
3. FastAPI sends request to LLM (Ollama)
4. LLM generates response
5. FastAPI returns response to user

---

## Why we need API

- Acts as a bridge between user and model
- Allows control (security, logging, validation)
- Enables future features (RAG, agents)

---

## Key Insight

Without API:
User → LLM (no control ❌)

With API:
User → API → LLM (controlled ✅)