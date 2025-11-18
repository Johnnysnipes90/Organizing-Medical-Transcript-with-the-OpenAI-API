from medical_transcription_icd.extract import build_messages_for_extraction

def test_build_messages_for_extraction():
    m = build_messages_for_extraction("Patient with headache.")
    assert isinstance(m, list)
    assert "headache" in m[1]["content"].lower()