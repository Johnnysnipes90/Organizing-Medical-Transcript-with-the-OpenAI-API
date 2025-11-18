# Organizing-Medical-Transcript-with-the-OpenAI-API
By leveraging AI, unstructured natural language can be processed into organized data. This can reduce administrative tasks for healthcare professionals, freeing more time for direct patient care.  In this project, I'll help the medical team automate the extraction and interpretation of vital information from their transcripts using the OpenAI API
---

# Medical Transcription → ICD-10 Structuring Pipeline

A clean, modular Python project that converts raw medical transcriptions into structured fields and maps recommended treatments to ICD-10 codes using NLP.

## Features
- Modular pipeline (`src/medical_transcription_icd`)
- Function-calling extraction
- ICD-10 code mapping via language models
- Utility loaders
- Unit tests for core modules
- Notebook demo

## Usage
1. Place your CSV into `data/transcriptions.csv`
2. Install dependencies:

3. Run:
```python
from medical_transcription_icd.utils import load_transcriptions
from medical_transcription_icd.process import process_transcriptions

pip install -r requirements.txt

df = load_transcriptions()
df_struct = process_transcriptions(df)
print(df_struct.head())

## ✅ Two Interfaces  
- **CLI Application** (Rich-powered terminal UI)  
- **Streamlit Web App** (modern, beautiful, responsive)


---

# 🧰 Project Structure

```
medical-transcription-icd/
├─ data/                      # not committed; stores local CSV
├─ notebooks/
│  └─ example.ipynb
├─ src/
│  └─ medical_transcription_icd/
│     ├─ __init__.py
│     ├─ client.py
│     ├─ extract.py
│     ├─ icd.py
│     ├─ process.py
│     └─ utils.py
├─ tests/
│  ├─ test_extract.py
│  └─ test_icd.py
├─ .gitignore
├─ .pre-commit-config.yaml
├─ pyproject.toml
├─ requirements.txt
├─ setup.cfg
├─ README.md
├─ CONTRIBUTING.md
├─ CODE_OF_CONDUCT.md
├─ LICENSE
├─ Dockerfile
└─ Makefile
```