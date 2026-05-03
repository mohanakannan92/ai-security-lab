# Error Handling & Fixes

## 1. ModuleNotFoundError: No module named 'ollama'

### Cause
Ollama Python package not installed in virtual environment

### Fix
pip install ollama

### Lesson
Ollama CLI ≠ Python package  
Always install dependencies inside venv

---

## 2. Uvicorn not recognized

### Cause
Uvicorn not installed in virtual environment

### Fix
pip install uvicorn

---

## 3. Model not found

### Error
"model 'phi3' not found"

### Cause
Model not downloaded or running

### Fix
ollama run tinyllama

---

## 4. Memory Error (phi3)

### Error
Requires more memory than available

### Fix
Use smaller model:
- tinyllama

---

## 5. Git commit identity error

### Fix
git config --global user.email "your@email.com"
git config --global user.name "Your Name"