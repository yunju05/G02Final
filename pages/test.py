import streamlit as st
from gtts import gTTS
import os

# 스트림릿 앱 설정
st.title("Clickable Text-to-Speech")

# 예제 텍스트
text = "안녕하세요. 이 문장을 클릭하여 들어보세요."

# JavaScript를 사용하여 텍스트 클릭 이벤트 추가
st.markdown(f"""
    <script>
    function playAudio() {{
        var audio = new Audio('http://localhost:8501/audio');
        audio.play();
    }}
    </script>
    <p onclick="playAudio()" style="cursor: pointer; color: blue;">{text}</p>
""", unsafe_allow_html=True)

# TTS 변환 및 오디오 파일 저장
tts = gTTS(text=text, lang='ko')
tts.save("output.mp3")

# 오디오 재생
st.audio("output.mp3", format="audio/mp3")
