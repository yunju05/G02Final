import streamlit as st
from vosk import Model, KaldiRecognizer
import wave
import os

# 오디오 데이터를 처리할 백엔드가 있다고 가정한 예시
st.markdown("""
    <h2>음성 인식 예제</h2>
    <p>녹음을 시작하려면 버튼을 누르세요:</p>
    <button id="recordButton">녹음</button>
    <p id="status"></p>
    <script>
        const recordButton = document.getElementById('recordButton');
        const status = document.getElementById('status');
        
        recordButton.addEventListener('click', () => {
            // 여기에 녹음 기능 구현
            // 오디오 데이터를 서버로 전송하여 STT 처리
            status.textContent = '녹음 중...';
            // 녹음 후
            status.textContent = '처리 중...';
            // 처리 완료 후
            status.textContent = '완료!';
        });
    </script>
""", unsafe_allow_html=True)


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
