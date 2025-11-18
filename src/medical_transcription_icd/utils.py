"""
Utility functions: loading CSV.
"""
import pandas as pd
from pathlib import Path

def load_transcriptions(path="data/transcriptions.csv") -> pd.DataFrame:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"{path} not found. Place your CSV there.")
    return pd.read_csv(p)