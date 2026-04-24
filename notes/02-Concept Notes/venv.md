# Virtual Environment (venv)

## What it is
An isolated Python environment for each project.

---

## Why it exists
Avoid conflicts between different project dependencies.

---

## Example
Project A → fastapi v1  
Project B → fastapi v2  

Without venv → conflict  
With venv → isolated environments

---

## Commands

Create:
python -m venv venv

Activate:
.\venv\Scripts\Activate.ps1

Deactivate:
deactivate

---

## Key Insight
venv ensures:
- clean environment
- reproducibility
- safe experimentation