import streamlit as st
from vosk import Model, KaldiRecognizer
import wave
import os

# 모델 다운로드 및 로딩
if not os.path.exists("model"):
    st.write("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    st.stop()

model = Model("model")

st.title("Vosk Speech-to-Text Example")

uploaded_file = st.file_uploader("Upload a WAV file", type="wav")

if uploaded_file is not None:
    # Save uploaded file temporarily
    with open("temp.wav", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Open the WAV file
    wf = wave.open("temp.wav", "rb")
    rec = KaldiRecognizer(model, wf.getframerate())

    st.write("Transcription:")

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = rec.Result()
            st.text(result)

    final_result = rec.FinalResult()
    st.text(final_result)
