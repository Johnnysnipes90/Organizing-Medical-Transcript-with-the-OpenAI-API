"""
Pipeline orchestrator: extraction → ICD mapping → output dataframe.
"""
import pandas as pd
from typing import List, Dict
from .client import get_client
from .extract import build_messages_for_extraction, parse_extraction_response
from .icd import build_messages_for_icd_lookup, parse_icd_response

def process_transcriptions(df: pd.DataFrame, api_key: str = None) -> pd.DataFrame:
    client = get_client(api_key)
    results: List[Dict] = []

    for _, row in df.iterrows():
        transcription = row.get("transcription", "")
        specialty = row.get("medical_specialty", "")

        # Extraction
        messages = build_messages_for_extraction(transcription)
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=[{
                "type": "function",
                "function": {
                    "name": "extract_patient_info",
                    "description": "Extract patient info.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "age": {"type": "string"},
                            "treatment": {"type": "string"}
                        },
                        "required": ["age", "treatment"]
                    }
                }
            }]
        )

        extracted = parse_extraction_response(resp)
        age = extracted["age"]
        treatment = extracted["treatment"]

        # ICD lookup
        icd_messages = build_messages_for_icd_lookup(treatment)
        icd_resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=icd_messages
        )
        icd = parse_icd_response(icd_resp)

        results.append({
            "age": age,
            "recommended_treatment": treatment,
            "medical_specialty": specialty,
            "icd_code": icd.get("icd_code"),
            "icd_description": icd.get("description")
        })

    return pd.DataFrame(results)