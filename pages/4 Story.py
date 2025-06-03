import streamlit as st
import requests
import random
from urllib.parse import quote
from streamlit_drawable_canvas import st_canvas
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Story with Canvas", layout="centered")
st.write("⭐ Learning Story")


# 탭 구성
tab1, tab2, tab3 = st.tabs([
    "1. 📋Listen and Read", 
    "2. 🖍️Drawing Canvas",
    "3. 💬 Share Your Drawing"
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
# 🔈 Drawing Canvas with TTS
# -------------------
with tab2:
    st.header("🖍️ Drawing Canvas with Random Audio")
    st.markdown("""
    1. Click the **"🔄 Play Random Audio"** button to listen to a short part of the story.  
    2. Based on what you heard, draw a **four-panel comic (4컷 만화)** that matches the story.  
    3. Use the tools below to adjust **line thickness** and **color**.  
    4. When finished, download your comic and upload it in the next tab!
    """)

    # GitHub에 저장된 mp3 파일 URL 리스트 (실제 URL로 바꾸세요)
    audio_files = [
        "https://github.com/yunju05/G02Final/raw/main/pages/text%201.mp3",
        "https://github.com/yunju05/G02Final/raw/main/pages/text%202.mp3",
        "https://github.com/yunju05/G02Final/raw/main/pages/text%203.mp3"
    ]

    if "selected_audio_url" not in st.session_state:
        st.session_state.selected_audio_url = ""

    if st.button("🔄 Play Random Audio"):
        st.session_state.selected_audio_url = random.choice(audio_files)

    if st.session_state.selected_audio_url:
        try:
            response = requests.get(st.session_state.selected_audio_url)
            st.audio(response.content, format="audio/mp3")
        except Exception as e:
            st.error(f"오디오 재생 중 오류 발생: {e}")

    # 캔버스 설정
    stroke_width = st.slider("✏️ Line Thickness", 1, 25, 5)
    stroke_color = st.color_picker("🎨 Line Color", "#000000")

    if "canvas_key" not in st.session_state:
        st.session_state.canvas_key = 0

    if st.button("🔁 Reset Canvas"):
        st.session_state.canvas_key += 1

    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color="#FFFFFF",
        height=600,
        width=600,
        drawing_mode="freedraw",
        key=f"canvas_{st.session_state.canvas_key}",
    )

    if canvas_result.image_data is not None:
        img = canvas_result.image_data.astype("uint8")
        st.image(img, caption="🖼️ Your Drawing")

        buffered = BytesIO()
        Image.fromarray(img).save(buffered, format="PNG")

        st.download_button(
            label="📥 Download Your Drawing (PNG)",
            data=buffered.getvalue(),
            file_name="drawing.png",
            mime="image/png"
        )

with tab3:
    st.header("💬 Upload Your Drawings to Padlet")
    st.markdown(
        """
        Feel free to share your drawings by uploading them to our Padlet board below.  
        Please make sure to upload your drawing to the correct section based on your assigned story.   
        Each section is clearly labeled on the Padlet board for your convenience.
        """
    )
    padlet_url = "https://padlet.com/yunju05325/digital-classroom-l9dikrb4yijjudux"
    st.components.v1.iframe(padlet_url, height=500, scrolling=True)

