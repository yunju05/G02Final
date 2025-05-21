import streamlit as st
import requests

tab1, tab2 = st.tabs([
    "1. Listening to the story", 
    "2. Reading the story",
])

with tab1:
    st.title("Story Audio")

    def play_audio():
        st.write("Let's listen to the story!")

        # URL에서 파일 다운로드
        url = "https://github.com/yunju05/G02Final/raw/main/pages/audio_sample.mp3"
        response = requests.get(url)

        # 오디오 재생
        st.audio(response.content, format='audio/mp3')

    if __name__ == "__main__":
        play_audio()
