"""
ICD mapping module.
"""

def build_messages_for_icd_lookup(treatment_text: str) -> list:
    return [
        {"role": "system",
         "content": "Return ICD-10 code as JSON: {\"icd_code\": \"<CODE>\", \"description\": \"<DESC>\"}"},
        {"role": "user", "content": treatment_text}
    ]

def parse_icd_response(response):
    content = response.choices[0].message.content
    try:
        import json
        return json.loads(content)
    except Exception:
        return {"icd_code": content, "description": ""}