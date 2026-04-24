# Day 01 – Setup & First API

## Problem
1. 'ollama' not recognized
2. venv activation failed
3. uvicorn not recognized
4. main.py not found

---

## What I tried
- Ran commands in PowerShell
- Tried activating venv directly
- Ran uvicorn without installing dependencies

---

## What worked

### Fix 1: venv activation
Command:
.\venv\Scripts\Activate.ps1

Fix:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

or 

(Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& c:\Mohanakannan\AI\source\repo\ai-security-lab\venv\Scripts\Activate.ps1)

---
### Fix 2: Ollama not recognized
- Installed Ollama properly in venv 
- run cmd "ollama run tinyllama"
---

### Fix 3: uvicorn not recognized
Command:
pip install fastapi uvicorn requests

once venv comes up (i.e as per Fix 1) execute the cmd "uvicorn main:app --reload"

---

### Fix 4: main.py missing
- Created main.py manually
- Verified file exists using:
dir

---

## Why it works
- Tools must be installed inside virtual environment
- PowerShell blocks scripts by default (security restriction)
- Python apps require correct file structure

---

## Learning
- Always verify environment before running app
- Errors are normal — debugging is part of engineering