import streamlit as st
import requests

    def play_audio():
        st.write("Let's listen to the story!")

        # URL에서 파일 다운로드
        url = "https://github.com/yunju05/G02Final/raw/main/pages/audio_sample.mp3"
        response = requests.get(url)

        # 오디오 재생
        st.audio(response.content, format='audio/mp3')

    if __name__ == "__main__":
        play_audio()

    st.markdown("### 🌳 The Whispering Woods")
    st.markdown("""
    Leo and his friends discovered a path leading to the Whispering Woods, known for the trees that could talk. The locals avoided it, saying it was bewitched, but the adventurous teens couldn’t resist exploring.

    As they walked deeper into the woods, the trees started whispering. Each tree told stories of ancient times, of battles fought and lovers separated. The trees also warned them about the dangers of forgetting the past and the importance of nature.

    Moved by these stories, the friends promised to protect the woods and share their knowledge. They left the woods wiser, with a deeper respect for nature and its untold stories, ready to advocate for its preservation.
    """)
    st.image("https://github.com/MK316/Digital-Literacy-Class/blob/main/materials/story02.png?raw=true", caption="A mystical forest path under a twilight sky, with towering trees whose leaves rustle in the wind. Silhouettes of teenagers stand listening intently to the trees, faces illuminated by a soft, eerie glow from the trees.")
