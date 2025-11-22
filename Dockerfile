# ============================================
# Stage 1 — Build environment
# ============================================
FROM python:3.10-slim AS base

# Set working directory
WORKDIR /app

# Install system packages (needed for pandas, numpy, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY ./src ./src
COPY ./streamlit_app.py .
COPY ./requirements.txt .
COPY ./notebooks ./notebooks
COPY ./data ./data

# Install dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Create a non-root user for security
RUN useradd -m appuser
USER appuser

# Default exposes for Streamlit + Jupyter
EXPOSE 8501
EXPOSE 8888

# ============================================
# Default command (Streamlit app)
# ============================================
CMD ["streamlit", "run", "streamlit_app.py"]