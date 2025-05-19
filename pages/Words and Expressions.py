import streamlit as st
import pandas as pd
import os
from gtts import gTTS
import base64
import tempfile

st.set_page_config(page_title="📚 TTS Word Study", layout="centered")

st.title("🔊 Study Words with Audio")

# Path to CSV file
csv_path = "data/word.csv"

# TTS playback function
def play_tts(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        audio_path = fp.name

    with open(audio_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
        b64 = base64.b64encode(audio_bytes).decode()
        audio_html = f"""
            <audio controls autoplay>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)

# Load CSV
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)

    if 'Word' not in df.columns or 'Meaning' not in df.columns:
        st.error("The CSV file must contain 'Word' and 'Meaning' columns.")
    else:
        st.success("✅ Word file loaded successfully!")

        tab1, tab2 = st.tabs(["📘 Basic Learning", "🚀 Advanced Practice"])

        with tab1:
            st.markdown("### Listen and Learn")
            for idx, row in df.iterrows():
                st.markdown(f"**{row['Word']}** — {row['Meaning']}")
                if st.button(f"🔊 Hear Word {idx}", key=f"en_{idx}"):
                    play_tts(row['Word'], lang="en")
                st.markdown("---")

        with tab2:
            st.markdown("### Advanced Practice (Coming Soon)")
            st.info("This tab is reserved for more advanced learning tools, such as quizzes or writing practice.")
else:
    st.error(f"File `{csv_path}` not found. Please make sure it exists.")
