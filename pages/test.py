import streamlit as st
from gtts import gTTS

# 여러 문장 정의
texts = [
    "안녕하세요. 이 문장을 클릭하여 들어보세요.",
    "이것은 두 번째 문장입니다.",
    "여기 세 번째 문장이 있습니다."
]

# 각 문장에 대해 TTS 생성 및 Streamlit의 audio 기능 사용
for i, text in enumerate(texts):
    # TTS 변환 및 오디오 파일 저장
    tts = gTTS(text=text, lang='ko')
    filename = f"output_{i}.mp3"
    tts.save(filename)
    
    # 텍스트와 오디오 버튼을 함께 표시
    st.write(text)
    st.audio(filename, format="audio/mp3", start_time=0)
