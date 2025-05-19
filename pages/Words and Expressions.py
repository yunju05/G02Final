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

# TTS player
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

# Load word list
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)

    if 'Word' not in df.columns or 'Meaning' not in df.columns:
        st.error("The CSV file must contain 'Word' and 'Meaning' columns.")
    else:
        st.success("✅ Word file loaded successfully!")

        st.markdown("## ✏️ Learn Words")
        for idx, row in df.iterrows():
            st.markdown(f"**{row['Word']}** — {row['Meaning']}")
            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button(f"🔊 Hear Word {idx}", key=f"en_{idx}"):
                    play_tts(row['Word'], lang="en")
            with col2:
                if st.button(f"🔊 Hear Meaning {idx}", key=f"ko_{idx}"):
                    play_tts(row['Meaning'], lang="ko")
            st.markdown("---")
else:
    st.error(f"File `{csv_path}` not found. Please make sure it exists.")
