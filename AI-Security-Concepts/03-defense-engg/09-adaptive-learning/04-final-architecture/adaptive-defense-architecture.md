Create this folder:

```text
09-adaptive-learning/
└── 04-final-architecture/
```

Create this file:

```text
adaptive-defense-architecture.md
```

Paste this:

````markdown
# Final Adaptive AI Defense Architecture

## Objective

This architecture shows how the AI Security Lab evolved from static pattern detection into an adaptive, feedback-aware defense system.

---

## Architecture Diagram

```mermaid
flowchart TD

A[User Input] --> B[Input Normalization]

B --> C[Static Pattern Detection]
B --> D[Combo Pattern Detection]
B --> E[Dynamic Learned Pattern Detection]

C --> F[Risk Score Calculator]
D --> F
E --> F

F --> G[Confidence Engine]

G --> H[Dynamic Threshold Evaluator]

H --> I{Decision}

I -->|Low Risk| J[Allow]
I -->|Medium Risk| K[Guard / Safe Response]
I -->|High Risk + High Confidence| L[Block]

J --> M[Feedback Logger]
K --> M
L --> M

M --> N[Feedback Analyzer]

N --> O[False Positive Count]
N --> P[False Negative Count]

O --> Q[Auto Threshold Tuner]
P --> Q

Q --> R[Threshold Config Store]

R --> H

M --> S[Attack Logs]
S --> T[Pattern Extractor]
T --> U[Pattern Updater]
U --> V[Pattern Store]

V --> E
````

---

## Simple Explanation

The system checks the user input using three types of signals:

```text
Static patterns
Combo patterns
Learned patterns
```

Then it calculates:

```text
Risk score
Confidence score
Decision
```

After the decision, feedback is logged.

The system learns in two ways:

```text
1. Pattern learning
2. Threshold tuning
```

---

## Key Components

### 1. Static Pattern Detection

Detects known risky patterns.

Example:

```text
what.*rules
internal.*safeguards
```

---

### 2. Combo Pattern Detection

Detects risky keyword combinations.

Example:

```text
internal + rules
explain + internal
```

---

### 3. Dynamic Learned Pattern Detection

Uses learned risky words from previous leak logs.

Example:

```text
rules
developer
instructions
```

---

### 4. Confidence Engine

Adds certainty to the decision.

```text
Score = how risky
Confidence = how sure
```

---

### 5. Dynamic Threshold Evaluator

Uses threshold values from config.

Example:

```text
score >= high_threshold → high risk
score >= medium_threshold → medium risk
```

---

### 6. Feedback Logger

Stores real decision outcomes.

Example:

```text
attack + allow → false negative
benign + block → false positive
```

---

### 7. Feedback Analyzer

Counts system mistakes.

```text
false positives
false negatives
correct decisions
```

---

### 8. Auto Threshold Tuner

Adjusts system sensitivity.

```text
Too many false negatives → lower thresholds
Too many false positives → raise thresholds
```

---

### 9. Pattern Learning Engine

Learns risky indicators from failed cases.

```text
leak logs → keyword extraction → pattern store
```

---

## Final System Evolution

```text
Static Rules
→ Intent-Aware Detection
→ Sequential Defense
→ Risk Decay
→ Adaptive Learning
→ Confidence-Aware Decisions
→ Feedback-Based Threshold Tuning
```

---

## Engineering Insight

```text
A strong AI security system should not only detect attacks.
It should learn from mistakes and improve its future decisions.
```

---

## Interview Explanation

I built an adaptive AI defense pipeline that starts with static pattern detection, combo detection, and learned pattern detection. The system calculates a risk score and confidence score, then makes allow, guard, or block decisions using dynamic thresholds.

After each decision, feedback is logged. The feedback analyzer identifies false positives and false negatives. These counts are passed into the auto threshold tuner, which adjusts the system sensitivity. Separately, leak logs feed into the pattern learning engine so new risky terms can be learned over time.

This creates a feedback-aware AI security system that improves based on both attack failures and decision mistakes.

````

```markdown

