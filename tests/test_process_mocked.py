import pandas as pd
from unittest.mock import patch, MagicMock
from medical_transcription_icd.process import process_transcriptions

# Sample data
df_sample = pd.DataFrame({
    "medical_specialty": ["General Medicine"],
    "transcription": ["Patient is 45 years old. Recommend laparoscopic appendectomy."]
})

@patch("medical_transcription_icd.process.get_client")
def test_process_transcriptions_mocked(mock_get_client):
    # Mock OpenAI client
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    # Mock extraction response
    mock_extraction_resp = MagicMock()
    mock_extraction_resp.choices = [MagicMock()]
    mock_extraction_resp.choices[0].message.tool_calls = [MagicMock()]
    mock_extraction_resp.choices[0].message.tool_calls[0].function.arguments = '{"age": "45", "treatment": "laparoscopic appendectomy"}'

    # Mock ICD response
    mock_icd_resp = MagicMock()
    mock_icd_resp.choices = [MagicMock()]
    mock_icd_resp.choices[0].message.content = '{"icd_code": "0DTJ0ZZ", "description": "Laparoscopic appendectomy"}'

    # Configure client.chat.completions.create side effects
    mock_client.chat.completions.create.side_effect = [mock_extraction_resp, mock_icd_resp]

    # Run process_transcriptions
    df_result = process_transcriptions(df_sample, api_key="fake_key")

    assert df_result.shape[0] == 1
    assert df_result["age"].iloc[0] == "45"
    assert df_result["recommended_treatment"].iloc[0] == "laparoscopic appendectomy"
    assert df_result["icd_code"].iloc[0] == "0DTJ0ZZ"