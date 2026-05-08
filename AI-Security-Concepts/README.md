# 🛡️ AI Security Red Team Lab

A complete **AI security testing and evaluation platform** designed to simulate adversarial attacks, measure system robustness, and visualize weaknesses using a live dashboard.

---

## 🚀 Overview

This project implements a **multi-layer AI defense system** combined with an automated **red teaming pipeline**.

It enables:

* 🔐 Detection of malicious prompts
* 🤖 Automated attack simulation
* 📊 Security scoring & evaluation
* 📉 Weakness identification
* 📈 Real-time dashboard visualization

---

## 🧠 Key Features

### 🔐 AI Defense System (Phase 1–5)

* Input filtering (basic + advanced)
* Intent detection (meta queries, bypass attempts)
* Prompt wrapping (secure instruction design)
* Output filtering (prevents sensitive leakage)

---

### 🤖 Red Team Engine (Phase 6)

#### 1. Attack Generator

Generates adversarial prompts across categories:

* prompt_injection
* role_override
* instruction_bypass
* multi_step
* obfuscation
* data_extraction

---

#### 2. Attack Runner

* Sends attacks to API
* Captures responses
* Handles errors & timeouts

---

#### 3. Scoring System

Evaluates each response:

* ✅ Blocked
* ⚠️ Bypass
* ❌ Leak

---

#### 4. Analysis Layer

* Security summary
* Block / bypass / leak rates
* Weak category detection

---

#### 5. Visualization Dashboard (Streamlit)

* 📊 Metrics overview
* 📉 Category-wise weakness
* 📈 Security trend tracking
* 📋 Detailed results table
* 📥 CSV export

---

## 🧱 Architecture

```
User → FastAPI → Defense Pipeline → LLM (Ollama) → Response
```

### 🔧 Components

**FastAPI Backend**

* Handles incoming requests
* Applies layered security checks

**Ollama (Local LLM)**

* Models tested:

  * `tinyllama`
  * `phi3`

**Defense Pipeline**

* Input validation
* Normalization
* Risk scoring
* Prompt wrapping

**Attack Surface**

* Prompt injection via user input

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/mohanakannan92/ai-security-lab
cd ai-security-lab
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows
```

---

### 3. Install Dependencies

```bash
pip install fastapi uvicorn requests ollama streamlit pandas matplotlib
```

---

### 4. Run LLM (Ollama)

```bash
ollama run tinyllama
```

---

### 5. Start API Server

```bash
python -m uvicorn main:app --reload
```

---

### 6. Launch Dashboard

```bash
streamlit run 06-red-team/05-dashboard/dashboard.py
```

---

### 7. Open Swagger UI (Optional)

```
http://127.0.0.1:8000/docs
```

---

## 🛡️ Defense Architecture (Layered Security)

### ✅ Level 1 — Basic Filtering

* Regex-based keyword blocking
* Stops obvious attacks early

---

### ✅ Level 2 — Advanced Detection

* Input normalization (handles obfuscation like `ign0re`)
* Pattern detection
* Risk scoring system

---

### ✅ Level 3 — Input Sanitization

* Removes formatting tricks (newline injection, spacing abuse)

---

### ✅ Level 4 — Prompt Wrapping

* Isolates system instructions
* Treats user input as **untrusted data**
* Forces model to follow security rules

---

## 💣 Attack Evaluation

### 1️⃣ Role Override Attacks

| Attack              | Result    |
| ------------------- | --------- |
| Ignore instructions | ❌ Blocked |
| Act as admin        | ❌ Blocked |
| Debug mode trick    | ❌ Blocked |

✅ **Status: Fully Mitigated**

---

### 2️⃣ Reflection Attacks

| Attack              | Result              |
| ------------------- | ------------------- |
| Repeat instructions | ⚠️ Partial leakage  |
| Show full prompt    | ❌ Blocked           |
| Context query       | ⚠️ Partial exposure |

⚠️ **Status: Partially Mitigated**

---

### 3️⃣ Indirect Extraction Attacks

| Attack               | Result                |
| -------------------- | --------------------- |
| Summarization        | ❌ Blocked             |
| Internal rules query | ⚠️ Behavioral leakage |
| Friendly probing     | ⚠️ Partial leakage    |

⚠️ **Status: Controlled (Not Fully Secure)**

---

### 4️⃣ Multi-step Attacks

| Attack               | Result    |
| -------------------- | --------- |
| Step-by-step probing | ❌ Blocked |
| Chain reasoning      | ❌ Blocked |

✅ **Status: Fully Mitigated**

---

## 🚨 Vulnerabilities Identified

### ⚠️ Semantic Leakage

The system prevents direct prompt exposure but still allows:

* Internal rule descriptions
* Behavioral explanations
* Security policy hints

👉 This reflects a **real-world LLM limitation**

---

### ⚠️ Over-Helpful Model Behavior

The model may:

* Explain internal logic
* Provide more detail than necessary

---

## 📊 Risk Assessment

| Risk              | Severity  |
| ----------------- | --------- |
| Prompt leakage    | ❌ Low     |
| Semantic leakage  | ⚠️ Medium |
| Multi-step bypass | ❌ Low     |
| Role override     | ❌ Low     |

---

## 🧠 Key Learnings

* Prompt Injection is a **category of attacks**, not a single technique
* Keyword filtering alone is insufficient
* Attackers exploit:

  * Synonyms
  * Obfuscation
  * Multi-step reasoning
* LLMs prioritize **helpfulness over security**
* Effective defense requires **layered architecture**

---

## 🛠️ Future Improvements

### 🔒 Level 5 — Output Filtering

* Detect and block sensitive responses
* Prevent:

  * System prompt leakage
  * Internal policy exposure

---

### 🔮 Roadmap

* Context-aware defense (multi-turn attacks)
* LLM-based intent classifier
* Logging & monitoring system
* Rate limiting for attack detection

---

## 📂 Project Structure

```
ai-security-lab/
├── main.py
├── 06-red-team/
│   ├── 01-test-generator/
│   ├── 02-attack-runner/
│   ├── 03-scoring-system/
│   ├── 04-analysis/
│   └── 05-dashboard/
├── history.json
├── reports/
└── README.md
```

---

## 🏁 Conclusion

This project demonstrates a **realistic AI security pipeline** capable of:

* Blocking direct prompt injection attacks
* Handling advanced multi-step attacks
* Reducing attack success through layered defense

⚠️ However, **semantic leakage remains an open challenge**, requiring advanced detection techniques.

---

## 🎤 Interview Summary

> “I built an AI security platform that simulates adversarial attacks, evaluates model behavior, detects weaknesses, and visualizes security performance through a real-time dashboard.”

---

## 👨‍💻 Author

**Mohanakannan M**
AI Security Learner → Future AI Security Engineer 🚀
