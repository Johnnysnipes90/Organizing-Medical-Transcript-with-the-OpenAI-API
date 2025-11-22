# Organizing-Medical-Transcript-with-the-OpenAI-API

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-green.svg)](https://platform.openai.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B.svg)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Project Type](https://img.shields.io/badge/Type-Portfolio%20Project-orange.svg)](https://github.com/Johnnysnipes90)

By leveraging AI, unstructured natural language can be processed into organized data. This can reduce administrative tasks for healthcare professionals, freeing more time for direct patient care.  In this project, I'll help the medical team automate the extraction and interpretation of vital information from their transcripts using the OpenAI API.


---
# Medical Transcription → ICD-10 Structuring Pipeline

Healthcare professionals spend hours daily extracting structured data from messy, natural-language medical transcripts.
This project automates that workflow using the OpenAI API, producing structured key fields:

- Patient age
- Recommended treatment or procedure
- Medical specialty
- Automatically matched ICD-10 code

All wrapped in a clean, modular, production-ready pipeline suitable for machine learning engineers, data engineers, and AI research roles.
--- 
## Features
✅ Modular architecture (industry-standard src/ layout)
✅ OpenAI function calling for structured extraction
✅ Automated ICD-10 code inference using LLMs
✅ CLI Tool → python -m medical_transcription_icd …
✅ Streamlit App for interactive processing
✅ Docker containerization
✅ Mocked unit tests (no real API calls in CI)
✅ Jupyter Notebook demo
✅ Extremely professional GitHub-ready project structure

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
├─ data/                      # local CSV storage (ignored by Git)
├─ notebooks/
│  └─ example.ipynb           # Demonstration notebook
├─ src/
│  └─ medical_transcription_icd/
│     ├─ __init__.py
│     ├─ client.py            # OpenAI client init
│     ├─ extract.py           # Function-calling extraction logic
│     ├─ icd.py               # ICD-10 mapping logic
│     ├─ process.py           # Full pipeline
│     └─ utils.py             # Helpers/loaders
├─ tests/
│  ├─ test_extract.py
│  ├─ test_icd.py
│  └─ test_process_mocked.py  # mocked OpenAI responses
├─ streamlit_app.py           # Web UI
├─ requirements.txt
├─ Dockerfile
├─ docker-compose.yml
├─ .pre-commit-config.yaml
├─ LICENSE
├─ README.md
└─ pyproject.toml / setup.cfg
```
---
# ⚙️ Installation
1️⃣ Clone the repository
```git clone https://github.com/your-username/medical-transcription-icd.git
cd medical-transcription-icd```

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Set your OpenAI API key
export OPENAI_API_KEY=your_key_here     # macOS/Linux
setx OPENAI_API_KEY "your_key_here"     # Windows

📘 Usage Examples
✔ Python Usage
from medical_transcription_icd.utils import load_transcriptions
from medical_transcription_icd.process import process_transcriptions

df = load_transcriptions("data/transcriptions.csv")
df_structured = process_transcriptions(df)

print(df_structured.head())

✔ CLI Tool

Process a CSV directly:

python -m medical_transcription_icd.cli \
  --input data/transcriptions.csv \
  --output data/structured_output.csv

✔ Streamlit App
streamlit run streamlit_app.py


Then open:

http://localhost:8501

# 🐳 Docker Usage
Build
docker build -t medical-transcription-icd .

Run Streamlit App
docker run -p 8501:8501 -e OPENAI_API_KEY=$OPENAI_API_KEY medical-transcription-icd

Run CLI in Docker
docker run -it \
  -e OPENAI_API_KEY=$OPENAI_API_KEY \
  medical-transcription-icd \
  --input data/transcriptions.csv \
  --output data/out.csv

# 🧪 Testing

All OpenAI calls are mocked, so tests run without internet/APIs.

Run tests:

pytest -q

📒 Notebook Demo

Launch the notebook:

jupyter notebook notebooks/example.ipynb