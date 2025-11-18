from medical_transcription_icd.icd import build_messages_for_icd_lookup

def test_build_messages_for_icd_lookup():
    m = build_messages_for_icd_lookup("appendectomy")
    assert "appendectomy" in m[1]["content"].lower()