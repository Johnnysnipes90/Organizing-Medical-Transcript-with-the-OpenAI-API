"""
Extraction module using function calling.
"""
from typing import Dict
import json

EXTRACTION_TOOL = [
    {
        "type": "function",
        "function": {
            "name": "extract_patient_info",
            "description": "Extract patient age and recommended treatment.",
            "parameters": {
                "type": "object",
                "properties": {
                    "age": {"type": "string"},
                    "treatment": {"type": "string"}
                },
                "required": ["age", "treatment"]
            }
        }
    }
]

def build_messages_for_extraction(transcription: str) -> list:
    return [
        {"role": "system",
         "content": "Extract patient age and recommended treatment from transcription."},
        {"role": "user", "content": transcription}
    ]

def parse_extraction_response(response) -> Dict[str, str]:
    try:
        args = response.choices[0].message.tool_calls[0].function.arguments
        return json.loads(args)
    except Exception as e:
        raise ValueError("Invalid extraction response format.") from e