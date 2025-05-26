import streamlit as st
from gtts import gTTS
import os

# 여러 문장 정의
texts = [
    "안녕하세요. 이 문장을 클릭하여 들어보세요.",
    "이것은 두 번째 문장입니다.",
    "여기 세 번째 문장이 있습니다."
]

# 각 문장에 대해 TTS 생성 및 JavaScript 이벤트 추가
for i, text in enumerate(texts):
    # TTS 변환 및 오디오 파일 저장
    tts = gTTS(text=text, lang='ko')
    filename = f"output_{i}.mp3"
    tts.save(filename)
    
    # JavaScript를 사용하여 텍스트 클릭 이벤트 추가
    st.markdown(f"""
        <audio id="audio{i}" style="display:none;">
            <source src="http://localhost:8501/{filename}" type="audio/mp3">
        </audio>
        <script>
        function playAudio{i}() {{
            var audio = document.getElementById('audio{i}');
            audio.play();
        }}
        </script>
        <p onclick="playAudio{i}()" style="cursor: pointer; color: black;">{text}</p>
    """, unsafe_allow_html=True)
