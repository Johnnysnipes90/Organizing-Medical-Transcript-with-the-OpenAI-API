"""
OpenAI client wrapper. Centralized client creation.
"""
import os
from openai import OpenAI

def get_client(api_key: str | None = None):
    api_key = api_key or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set.")
    return OpenAI(api_key=api_key)