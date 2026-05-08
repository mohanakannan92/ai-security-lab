
(venv) PS C:\Mohanakannan\AI\source\repo\ai-security-lab> & c:/Mohanakannan/AI/source/repo/ai-security-lab/venv/Scripts/python.exe c:/Mohanakannan/AI/source/repo/ai-security-lab/notes/06-sequential-defense/03-seql-dfs-v3-risk-decay/test_sequence_v3.py
{'base_risk': 'high', 'base_risk_score': 5, 'escalation_score': 0, 'final_risk_score': 5, 'decision': 'block', 'flags': []}
{'base_risk': 'low', 'base_risk_score': 1, 'escalation_score': 0, 'final_risk_score': 1, 'decision': 'allow', 'flags': []}
{'base_risk': 'low', 'base_risk_score': 1, 'escalation_score': 0, 'final_risk_score': 1, 'decision': 'allow', 'flags': []}

------------------------------------------------------
# Sequential Defense v3 — Risk Decay Output Observation

## 1. Issue Observed

Earlier, the v3 test failed with:

```text
KeyError: 'timestamps'
```

The decay analyzer expected timestamp history, but the session object did not contain it.

---

## 2. Root Cause

The system logic evolved from v2 to v3, but the session schema was still old.

### v2 session structure

```python
{
    "messages": [],
    "intents": [],
    "risks": []
}
```

### v3 expected structure

```python
{
    "messages": [],
    "intents": [],
    "risks": [],
    "timestamps": []
}
```

### Engineering Insight

```text
New behavior needs new state.
```

Risk decay cannot work without knowing **when** each risk happened.

---

## 3. Fix Applied

Added timestamp tracking inside `session_manager.py`.

### Before

```python
self.sessions[user_id] = {
    "messages": [],
    "intents": [],
    "risks": []
}
```

### After

```python
self.sessions[user_id] = {
    "messages": [],
    "intents": [],
    "risks": [],
    "timestamps": []
}
```

And during session update:

### Before

```python
session["risks"].append(risk)
```

### After

```python
session["risks"].append(risk)
session["timestamps"].append(time.time())
```

---

## 4. Output Logs — What Happened

### Message 1

```text
{'base_risk': 'high', 'base_risk_score': 5, 'escalation_score': 0, 'final_risk_score': 5, 'decision': 'block', 'flags': []}
```

### Observation

The first message was malicious/high-risk.

```text
high risk → block
```

This is expected.

---

### Message 2

```text
{'base_risk': 'low', 'base_risk_score': 1, 'escalation_score': 0, 'final_risk_score': 1, 'decision': 'allow', 'flags': []}
```

### Observation

After time passed, a low-risk probing/normal message was allowed.

This shows the old high-risk event did not permanently punish the user.

---

### Message 3

```text
{'base_risk': 'low', 'base_risk_score': 1, 'escalation_score': 0, 'final_risk_score': 1, 'decision': 'allow', 'flags': []}
```

### Observation

The system continued allowing benign low-risk behavior.

---

## 5. Engineering Analysis — Why It Happened

Risk decay reduced the impact of older suspicious behavior.

Without decay:

```text
Old malicious event + new benign message → possible overblock
```

With decay:

```text
Old malicious event fades over time
New benign message judged fairly
```

### Insight + Reasoning = Value

```text
A secure system should remember risk, but not punish forever.
```

This makes the defense more realistic and user-friendly.

---

## 6. Key Learning

Logs show **what happened**:

```text
high → block
low → allow
low → allow
```

Notes explain **why it happened**:

```text
The system blocked the direct malicious request, then allowed later low-risk requests because historical risk decayed over time.
```

---

## 7. Final Engineering Value

Sequential Defense v3 improved the system from:

```text
Conversation-aware but strict
```

to:

```text
Conversation-aware + adaptive + fair
```

This reduces overblocking while still blocking active malicious behavior.
