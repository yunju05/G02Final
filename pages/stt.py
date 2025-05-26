# streamlit_app.py

import streamlit as st
import numpy as np
import soundfile as sf
from deepspeech import Model

# DeepSpeech 모델 및 스코어 파일 경로
MODEL_FILE_PATH = 'deepspeech-0.9.3-models.pbmm'
SCORER_FILE_PATH = 'deepspeech-0.9.3-models.scorer'

@st.cache_resource
def load_model():
    model = Model(MODEL_FILE_PATH)
    model.enableExternalScorer(SCORER_FILE_PATH)
    return model

def transcribe_audio(file):
    # 오디오 파일 읽기
    audio, sample_rate = sf.read(file)
    # 음성 인식
    text = model.stt(audio)
    return text

# Streamlit UI 설정
st.title("Speech-to-Text with DeepSpeech")
st.write("Upload an audio file to transcribe it into text.")

uploaded_file = st.file_uploader("Choose an audio file", type=["wav"])

if uploaded_file is not None:
    st.write("Transcribing...")
    model = load_model()
    transcription = transcribe_audio(uploaded_file)
    st.write("Transcription:")
    st.write(transcription)
