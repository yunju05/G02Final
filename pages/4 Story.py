import streamlit as st
import requests
from streamlit_drawable_canvas import st_canvas
import numpy as np

st.write("⭐ Learning Story")

tab1, tab2 = st.tabs([
    "1. 📋Listen and Read", 
    "2. 🔈Drawing Canvas"
])

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

with tab2:
    st.title("Streamlit 그림판 (굵기 & 색깔 변경 가능)")

   import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np

def main():
    st.title("Streamlit 그림판 (굵기 & 색깔 변경 가능)")

    # 사용자 입력 위젯
    stroke_width = st.slider("선 굵기", min_value=1, max_value=25, value=5)
    stroke_color = st.color_picker("선 색깔", "#000000")

    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # 투명 오렌지색 배경
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color="#eeeeee",
        height=400,
        width=600,
        drawing_mode="freedraw",
        key="canvas",
    )

    if canvas_result.image_data is not None:
        img = canvas_result.image_data.astype(np.uint8)
        st.image(img)

if __name__ == "__main__":
    main()
