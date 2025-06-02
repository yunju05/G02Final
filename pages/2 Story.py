import streamlit as st
import requests

st.title("Listen and Read")

def play_audio():
    st.write("Click to play an audio.")

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
    
    st.image(
        "https://github.com/MK316/Digital-Literacy-Class/blob/main/materials/story02.png?raw=true", 
        caption="A mystical forest path under a twilight sky, with towering trees whose leaves rustle in the wind. Silhouettes of teenagers stand listening intently to the trees, faces illuminated by a soft, eerie glow from the trees."
    )

pip install streamlit streamlit-drawable-canvas

import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("Streamlit 그림판 기능")

# 캔버스 설정
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # 투명한 오렌지색으로 채우기
    stroke_width=5,
    stroke_color="#000000",
    background_color="#eee",
    height=400,
    width=600,
    drawing_mode="freedraw",
    key="canvas",
)

# 그려진 이미지 출력
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data)

