import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO
import random

st.write("⭐ Word and Expression")

tab1, tab2, tab3, tab4 = st.tabs(["1. Word list", "2. Listen to the word", "3. Spelling quiz", "4. TBA"])

######### TAB 1


with tab1:
  st.markdown("### ⭐ Word and Expression")

   # Load CSV from GitHub (update the link below)
  url = "https://github.com/yunju05/G02Final/raw/main/data/word.csv"
  df = pd.read_csv(url)

    # Show table only when button is clicked
  if st.button("Show Word List"):
     st.dataframe(df, use_container_width=True)


######### TAB 2 

with tab2:

  st.title("🎵 Listen to the word")
  
  # --- Load CSV from GitHub ---

  url = "https://github.com/yunju05/G02Final/raw/main/data/word.csv"  # ← replace this!
  df = pd.read_csv(url)
  
  # --- Dropdown to select word ---
  st.markdown("## Select a word to hear its pronunciation")
  selected_word = st.selectbox("Choose a word:", df["Word"].dropna().unique())
  
  # --- Generate and play audio ---
  if selected_word:
      tts = gTTS(selected_word, lang='en')
      audio_fp = BytesIO()
      tts.write_to_fp(audio_fp)
      audio_fp.seek(0)
      st.audio(audio_fp, format='audio/mp3')


######### TAB 3

with tab3:
    st.markdown("### 🎧 Listen and Type the Word")
    st.caption("Click the button to hear a word. Then type it and press 'Check the answer'.")

    # Load CSV
    url = "https://github.com/yunju05/G02Final/raw/main/data/word.csv"  # Replace this!
    df = pd.read_csv(url)
    word_list = df["Word"].dropna().tolist()

    # Initialize session state variables
    if "current_word" not in st.session_state:
        st.session_state.current_word = None
    if "audio_data" not in st.session_state:
        st.session_state.audio_data = None
    if "user_input" not in st.session_state:
        st.session_state.user_input = ""
    if "check_clicked" not in st.session_state:
        st.session_state.check_clicked = False

    # ▶️ Button to select and play a new random word
    if st.button("🔊 Let me listen to a word"):
        st.session_state.current_word = random.choice(word_list)
        st.session_state.user_input = ""
        st.session_state.check_clicked = False

        tts = gTTS(st.session_state.current_word, lang='en')
        audio_fp = BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        st.session_state.audio_data = audio_fp.read()

    # 🎧 Audio playback
    if st.session_state.audio_data:
        st.audio(st.session_state.audio_data, format='audio/mp3')

    # ✏️ Text input
    st.session_state.user_input = st.text_input("Type the word you heard:", value=st.session_state.user_input)

    # ✅ Check answer button
    if st.button("✅ Check the answer"):
        st.session_state.check_clicked = True

    # 💬 Give feedback only after clicking the check button
    if st.session_state.check_clicked and st.session_state.current_word:
        if st.session_state.user_input.strip().lower() == st.session_state.current_word.lower():
            st.success("✅ Correct!")
        else:
            st.error("❌ Try again.")

######### TAB 4

with tab4:
    st.markdown("### 🧠 Meaning to Word Quiz")
    st.caption("A random Korean meaning will be shown. Type the matching English word.")

    # Load CSV
    url = "https://github.com/yunju05/G02Final/raw/main/data/word.csv"
    df = pd.read_csv(url)

    # Initialize session state
    if "quiz_meaning" not in st.session_state:
        st.session_state.quiz_meaning = None
    if "quiz_answer" not in st.session_state:
        st.session_state.quiz_answer = None
    if "quiz_user_input" not in st.session_state:
        st.session_state.quiz_user_input = ""
    if "quiz_check_clicked" not in st.session_state:
        st.session_state.quiz_check_clicked = False

    # 🎲 Generate new quiz
    if st.button("🎯 New Quiz"):
        row = df.sample(1).iloc[0]
        st.session_state.quiz_meaning = row["Meaning"]
        st.session_state.quiz_answer = row["Word"]
        st.session_state.quiz_user_input = ""
        st.session_state.quiz_check_clicked = False

    # 🧾 Show quiz
    if st.session_state.quiz_meaning:
        st.markdown(f"**Korean meaning:** `{st.session_state.quiz_meaning}`")
        st.session_state.quiz_user_input = st.text_input("Write the English word:", value=st.session_state.quiz_user_input)

        if st.button("✅ Check answer"):
            st.session_state.quiz_check_clicked = True

        if st.session_state.quiz_check_clicked:
            if st.session_state.quiz_user_input.strip().lower() == st.session_state.quiz_answer.lower():
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Incorrect. The correct word was **{st.session_state.quiz_answer}**.")
    else:
        st.info("Click '🎯 New Quiz' to start.")
