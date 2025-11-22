# streamlit_app.py

import streamlit as st
import pandas as pd
from medical_transcription_icd.process import process_transcriptions
from medical_transcription_icd.utils import load_transcriptions

st.title("Medical Transcription → ICD-10")

uploaded_file = st.file_uploader("Upload CSV of transcriptions", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Preview of uploaded CSV")
    st.dataframe(df.head())

    if st.button("Process Transcriptions"):
        with st.spinner("Processing..."):
            df_structured = process_transcriptions(df)
        st.subheader("Structured Output")
        st.dataframe(df_structured)
        st.download_button(
            "Download CSV",
            df_structured.to_csv(index=False),
            file_name="structured_transcriptions.csv",
            mime="text/csv"
        )