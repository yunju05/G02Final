import streamlit as st
import requests
from streamlit_drawable_canvas import st_canvas
import numpy as np
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Story with Canvas", layout="centered")
st.write("⭐ Learning Story")

# 탭 구성
tab1, tab2 = st.tabs([
    "1. 📋Listen and Read", 
    "2. 🔈Drawing Canvas"
])

# -------------------
# 📋 Listen and Read
# -------------------
with tab1:
    st.title("Listen and Read")

    def play_audio():
        st.write("Click to play an audio.")
        url = "https://github.com/yunju05/G02Final/raw/main/pages/audio_sample.mp3"
        response = requests.get(url)
        st.audio(response.content, format='audio/mp3')

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

# -------------------
# 🔈 Drawing Canvas
# -------------------
with tab2:
    st.title("Streamlit 그림판")

    stroke_width = st.slider("선 굵기", 1, 25, 5)
    stroke_color = st.color_picker("선 색깔", "#000000")

    # 지우기 버튼 처리
    if st.button("🧹 지우기"):
        st.session_state.canvas_key = st.session_state.get("canvas_key", 0) + 1
    else:
        st.session_state.canvas_key = st.session_state.get("canvas_key", 0)

    # 캔버스
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color="#FFFFFF",
        height=400,
        width=600,
        drawing_mode="freedraw",
        key=f"canvas_{st.session_state.canvas_key}",
        update_streamlit=True
    )
