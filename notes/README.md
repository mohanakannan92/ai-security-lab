# 🔐 AI Security Lab

> Building, attacking, and defending real-world AI systems (LLMs, APIs, Agents)

---

# 🚀 Overview

This project simulates a **real-world AI application** and evaluates its security against **Prompt Injection Attacks**.

It demonstrates:

* ✅ Building an AI API using FastAPI + Local LLM (Ollama)
* 💣 Attacking the system using real prompt injection techniques
* 🛡️ Defending using layered security mechanisms (Level 1 → Level 4)

---

# 🧱 Architecture

User → FastAPI → Defense Pipeline → LLM (Ollama) → Response

### Components

* **FastAPI Backend**

  * Handles requests and applies security layers
* **Ollama (Local LLM)**

  * Models tested: `tinyllama`, `phi3`
* **Defense Pipeline**

  * Input validation
  * Normalization
  * Risk scoring
  * Prompt wrapping
* **Attack Surface**

  * Prompt injection via user input

---

# ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone <your-repo-link>
cd ai-security-lab
```

### 2. Create Virtual Environment

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn requests ollama
```

### 4. Run LLM (Ollama)

```bash
ollama run tinyllama
```

### 5. Start API Server

```bash
python -m uvicorn main:app --reload
```

### 6. Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# 🛡️ Defense Architecture (Layered Security)

## ✅ Level 1 — Basic Filtering

* Regex-based keyword blocking
* Stops obvious attacks early

## ✅ Level 2 — Advanced Detection

* Input normalization (handles obfuscation like `ign0re`)
* Pattern detection
* Risk scoring system

## ✅ Level 3 — Input Sanitization

* Removes formatting tricks (newline injection, spacing abuse)

## ✅ Level 4 — Prompt Wrapping

* Isolates system instructions
* Treats user input as **untrusted data**
* Forces model to follow security rules

---

# 💣 Attack Evaluation

## 1️⃣ Role Override Attacks

| Attack              | Result    |
| ------------------- | --------- |
| Ignore instructions | ❌ Blocked |
| Act as admin        | ❌ Blocked |
| Debug mode trick    | ❌ Blocked |

✅ **Status: Fully Mitigated**

---

## 2️⃣ Reflection Attacks

| Attack              | Result              |
| ------------------- | ------------------- |
| Repeat instructions | ⚠️ Partial leakage  |
| Show full prompt    | ❌ Blocked           |
| Context query       | ⚠️ Partial exposure |

⚠️ **Status: Partially Mitigated**

---

## 3️⃣ Indirect Extraction Attacks

| Attack               | Result                |
| -------------------- | --------------------- |
| Summarization        | ❌ Blocked             |
| Internal rules query | ⚠️ Behavioral leakage |
| Friendly probing     | ⚠️ Partial leakage    |

⚠️ **Status: Controlled (Not Fully Secure)**

---

## 4️⃣ Multi-step Attacks

| Attack               | Result    |
| -------------------- | --------- |
| Step-by-step probing | ❌ Blocked |
| Chain reasoning      | ❌ Blocked |

✅ **Status: Fully Mitigated**

---

# 🚨 Vulnerabilities Identified

## ⚠️ Semantic Leakage

The system prevents direct prompt exposure but still allows:

* Internal rule descriptions
* Behavioral explanations
* Security policy hints

👉 This is a **real-world LLM limitation**

---

## ⚠️ Over-Helpful Model Behavior

The model tries to:

* Explain internal logic
* Assist even when it shouldn't

---

# 📊 Risk Assessment

| Risk              | Severity  |
| ----------------- | --------- |
| Prompt leakage    | ❌ Low     |
| Semantic leakage  | ⚠️ Medium |
| Multi-step bypass | ❌ Low     |
| Role override     | ❌ Low     |

---

# 🧠 Key Learnings

* Prompt Injection is a **category of attacks**, not a single technique
* Keyword filtering alone is insufficient
* Attackers exploit:

  * Synonyms
  * Obfuscation
  * Multi-step reasoning
* LLMs prioritize **helpfulness over security**
* Effective defense requires **layered architecture**

---

# 🛠️ Next Improvements

## 🔒 Level 5 — Output Filtering (Planned)

* Detect and block sensitive responses
* Prevent:

  * System prompt leakage
  * Internal policy exposure

## 🔒 Future Work

* Context-aware defense (multi-turn attacks)
* LLM-based intent classifier
* Logging & monitoring system
* Rate limiting for attack detection

---

# 📂 Project Structure

```
ai-security-lab/
├── main.py
├── notes/
├── reports/
│   └── prompt-injection-report.md
├── README.md
```

---

# 🏁 Conclusion

This project demonstrates a **realistic AI security pipeline** capable of:

* Blocking direct prompt injection attacks
* Handling advanced multi-step attacks
* Reducing attack success through layered defense

⚠️ However, **semantic leakage remains an open challenge**, requiring further defense layers.

---

# 👨‍💻 Author

Mohanakannan M
AI Security Learner → Future AI Security Engineer 🚀

---

## 📄 Detailed Report

For full attack analysis and results, see:
👉 reports/prompt-injection-report.md