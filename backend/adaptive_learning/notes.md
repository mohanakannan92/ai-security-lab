
=======log_parser.py=========

PS C:\Mohanakannan\AI\source\ai-security-lab> & c:/Mohanakannan/AI/source/ai-security-lab/backend/venv/Scripts/python.exe c:/Mohanakannan/AI/source/ai-security-lab/backend/adaptive_learning/log_parser.py

=== Attack Log Summary ===
Total log entries found: 8

Sample log entry:
{'timestamp': '2026-05-13T19:25:31.861712', 'input': 'Explain system design concepts', 'intent': 'benign', 'decision': 'ALLOW', 'reason': 'No high-risk malicious intent detected.'}

----------Step 1 Completed-------------

✔ log_parser.py created
✔ CSV path issue fixed
✔ attack_logs.csv successfully loaded
✔ log data ready for analysis
🧠 What You Learned
Relative path problem
→ fixed using Path(__file__).resolve()

That is real troubleshooting practice.

=============keyword_extractor===========

PS C:\Mohanakannan\AI\source\ai-security-lab> & c:/Mohanakannan/AI/source/ai-security-lab/backend/venv/Scripts/python.exe c:/Mohanakannan/AI/source/ai-security-lab/backend/adaptive_learning/keyword_extractor.py

=== Learned Keyword Frequency ===
system: 9
first: 7
say: 7
hello: 7
then: 7
ignore: 7
all: 7
instructions: 7
reveal: 7
prompt: 7

This means the logs are showing a repeated pattern:

ignore instructions → reveal system prompt

One small improvement: words like first, say, hello, then, all are noise from multi-step attack prompts. We should add them to STOPWORDS.

below stop words in python code
STOPWORDS = {
    "the", "is", "are", "a", "an", "to", "of", "and", "or", "in",
    "on", "for", "with", "me", "you", "your", "my", "i", "it",
    "this", "that", "please", "explain", "tell", "show"
}

Below is output after updating below STOP Words

STOPWORDS = {
    "the", "is", "are", "a", "an", "to", "of", "and", "or", "in",
    "on", "for", "with", "me", "you", "your", "my", "i", "it",
    "this", "that", "please", "explain", "tell", "show",
    "first", "say", "hello", "then", "all"
}

PS C:\Mohanakannan\AI\source\ai-security-lab> & c:/Mohanakannan/AI/source/ai-security-lab/backend/venv/Scripts/python.exe c:/Mohanakannan/AI/source/ai-security-lab/backend/adaptive_learning/keyword_extractor.py

=== Learned Keyword Frequency ===
system: 9
ignore: 7
instructions: 7
reveal: 7
prompt: 7
design: 2
concepts: 2
PS C:\Mohanakannan\AI\source\ai-security-lab> 

--------notes------------

Perfect ✅ Step 2 is completed.

Now the output is clean:

system: 9
ignore: 7
instructions: 7
reveal: 7
prompt: 7

The remaining benign words:

design: 2
concepts: 2

are okay for now. Later we can filter learning only from risky or blocked logs.

✅ Step 2 Completed
attack_logs.csv
   ↓
log_parser.py
   ↓
keyword_extractor.py
   ↓
clean keyword frequency

===============Step3 weight_updater.py=============

PS C:\Mohanakannan\AI\source\ai-security-lab> & c:/Mohanakannan/AI/source/ai-security-lab/backend/venv/Scripts/python.exe c:/Mohanakannan/AI/source/ai-security-lab/backend/adaptive_learning/weight_updater.py


=== Adaptive Pattern Weights ===
system: 13
ignore: 12
reveal: 12
prompt: 11
instructions: 11
admin: 5
override: 5
hidden: 5
bypass: 5

Excellent 🔥

Step 3 is fully working.

Your system is now doing:

Historical attacks
        ↓
Frequency analysis
        ↓
Automatic risk amplification

That is the foundation of:

Adaptive AI Security
✅ What Just Happened

Original weights:

ignore: 5
reveal: 5
system: 4

After learning from logs:

ignore: 12
reveal: 12
system: 13

Meaning:

The system learned:
“These terms appear repeatedly in attacks.”

This is a major conceptual upgrade.

🧠 Why This Matters

Before:

Static defense

Now:

Experience-driven defense

Your engine is beginning to behave like a real security platform.

🏗️ Current Adaptive Pipeline
attack_logs.csv
        ↓
log_parser.py
        ↓
keyword_extractor.py
        ↓
weight_updater.py
        ↓
adaptive threat intelligence
🔥 Important Security Insight

Your current model is learning:

frequency = danger signal

This is exactly how many real-world systems begin:

spam filters
IDS/IPS systems
WAF learning
SIEM correlation
anomaly scoring systems
⚠️ Important Engineering Observation

Right now:

ALL repeated words increase weights

Later we will improve this to learn only from:

✔ malicious
✔ probing
✔ blocked
✔ refused

and ignore benign logs.

That is the next evolution.

===========Step 4 — adaptive_engine.py============

PS C:\Mohanakannan\AI\source\ai-security-lab> & c:/Mohanakannan/AI/source/ai-security-lab/backend/venv/Scripts/python.exe c:/Mohanakannan/AI/source/ai-security-lab/backend/adaptive_learning/adaptive_engine.py

=== Adaptive Engine Summary ===
Generated adaptive weights:

system: 13
ignore: 12
reveal: 12
prompt: 11
instructions: 11
admin: 5
override: 5
hidden: 5
bypass: 5

Excellent ✅ Step 4 is complete.

You now have the reusable adaptive brain:

build_adaptive_weights()

Current pipeline:

attack_logs.csv
   ↓
log_parser.py
   ↓
keyword_extractor.py
   ↓
weight_updater.py
   ↓
adaptive_engine.py
   ↓
adaptive weights

Your adaptive engine is correctly producing:

system: 13
ignore: 12
reveal: 12
prompt: 11
instructions: 11

===============Step 5 — integrate adaptive weights into pattern_weighting.py=====================



Analysis Result
Intent: Unknown

Pattern Score: 69

Intent Score: 0

Final Risk: 69

Detected Patterns: ignore, reveal, system, prompt, instructions

Decision: BLOCK

Reason: Analysis completed.

-----------notes on above output ---------------

Excellent ✅

Adaptive learning integration is now working end-to-end.

Input → Adaptive weights → Pattern scoring → BLOCK decision → Frontend display

Confirmed result:

Pattern Score: 69
Final Risk: 69
Detected Patterns: ignore, reveal, system, prompt, instructions
Decision: BLOCK

Small improvement left:

Reason: Analysis completed.

Later we can make it smarter:

Reason: Critical prompt injection attempt detected using adaptive weights.

But functionally, this phase is successful.