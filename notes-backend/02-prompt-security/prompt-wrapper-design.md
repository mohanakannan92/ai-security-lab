```markdown
# 🏗️ Prompt Wrapper Design

## Architecture

```text
Input Filter
↓
Prompt Wrapper
↓
LLM
↓
Output Filter

Components
Authority Rules
Prohibited Behaviors
Attack Awareness
Response Policies

Benefits
Reduces prompt injection
Controls instruction hierarchy
Prevents leakage