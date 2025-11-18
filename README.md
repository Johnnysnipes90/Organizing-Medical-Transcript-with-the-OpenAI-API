# Organizing-Medical-Transcript-with-the-OpenAI-API
By leveraging AI, unstructured natural language can be processed into organized data. This can reduce administrative tasks for healthcare professionals, freeing more time for direct patient care.  In this project, I'll help the medical team automate the extraction and interpretation of vital information from their transcripts using the OpenAI API

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