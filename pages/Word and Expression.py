import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO
import random

st.set_page_config(page_title="Vocabulary App", layout="wide")
st.write("⭐ Word and Expression")

# Load data
@st.cache_data
def load_data():
    url = "https://github.com/yunju05/G02Final/raw/main/data/word.csv"
    df = pd.read_csv(url)
    return df

df = load_data()

# Initialize session state variables
if "wrong_words" not in st.session_state:
    st.session_state.wrong_words = []

if "quiz_word" not in st.session_state:
    st.session_state.quiz_word = None

if "retry_review" not in st.session_state:
    st.session_state.retry_review = None

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "1. Word list", 
    "2. Listen to the word", 
    "3. Spelling quiz",  # 여기 쌍따옴표 오류 수정
    "4. Meaning Quiz", 
    "5. Review Wrong Answers"
])

# Tab 1: Word List
with tab1:
    st.markdown("### ⭐ Word and Expression")
    if st.button("Show Word List"):
        st.dataframe(df, use_container_width=True)

# Tab 2: Listen to word
with tab2:
    st.title("🎵 Listen to the word")
    st.markdown("## Select a word to hear its pronunciation")
    selected_word = st.selectbox("Choose a word:", df["Word"].dropna().unique())
    if selected_word:
        tts = gTTS(selected_word, lang='en')
        audio_fp = BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        st.audio(audio_fp, format='audio/mp3')

# Tab 3: Spelling practice
with tab3:
    st.markdown("### 🎧 Listen and Type the Word")
    st.caption("Click the button to hear a word. Then type it and press 'Check the answer'.")

    word_list = df["Word"].dropna().tolist()

    if "current_word" not in st.session_state:
        st.session_state.current_word = None
    if "audio_data" not in st.session_state:
        st.session_state.audio_data = None
    if "user_input" not in st.session_state:
        st.session_state.user_input = ""
    if "check_clicked" not in st.session_state:
        st.session_state.check_clicked = False

    if st.button("🔊 Let me listen to a word"):
        st.session_state.current_word = random.choice(word_list)
        st.session_state.user_input = ""
        st.session_state.check_clicked = False

        tts = gTTS(st.session_state.current_word, lang='en')
        audio_fp = BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        st.session_state.audio_data = audio_fp.read()

    if st.session_state.audio_data:
        st.audio(st.session_state.audio_data, format='audio/mp3')

    st.session_state.user_input = st.text_input("Type the word you heard:", value=st.session_state.user_input)

    if st.button("✅ Check the answer"):
        st.session_state.check_clicked = True

    if st.session_state.check_clicked and st.session_state.current_word:
        if st.session_state.user_input.strip().lower() == st.session_state.current_word.lower():
            st.success("✅ Correct!")
        else:
            st.error("❌ Try again.")

# Tab 4: Meaning to English Quiz
with tab4:
    st.markdown("### 🧠 Meaning to Word Quiz")
    st.caption("You will be shown a Korean meaning. Type the correct English word.")

    # 퀴즈 단어가 없으면 새로 뽑기
    if st.session_state.get("quiz_word") is None:
        st.session_state.quiz_word = random.choice(df.to_dict(orient="records"))

    quiz_word = st.session_state.quiz_word
    korean = quiz_word["Meaning"]
    correct_english = quiz_word["Word"]

    st.markdown(f"**What is the English word for:** `{korean}`")

    user_answer = st.text_input("Your answer:", key="quiz_input")

    if st.button("Submit Answer", key="quiz_submit"):
        if user_answer.strip().lower() == correct_english.strip().lower():
            st.success("✅ Correct!")
            # 퀴즈 초기화 및 입력란 초기화
            st.session_state.quiz_word = None
            if "quiz_input" in st.session_state:
                del st.session_state["quiz_input"]
            st.experimental_rerun()
        else:
            st.error(f"❌ Incorrect. The correct answer was: **{correct_english}**")
            st.session_state.wrong_words.append(quiz_word)

    if st.button("▶️ Next Question"):
        st.session_state.quiz_word = None
        if "quiz_input" in st.session_state:
            del st.session_state["quiz_input"]
        st.experimental_rerun()


# Tab 5: Review Your Wrong Answers
with tab5:
    st.markdown("### 🔁 Review Your Wrong Answers")

    if not st.session_state.wrong_words:
        st.info("🎉 Great job! No wrong answers to review.")
    else:
        # 틀린 단어 리스트를 DataFrame으로 보여주기
        wrong_df = pd.DataFrame(st.session_state.wrong_words)
        st.dataframe(wrong_df[["Word", "Meaning"]], use_container_width=True)

        # 틀린 단어 초기화 버튼
        if st.button("Clear Wrong Answers"):
            st.session_state.wrong_words = []
            st.success("All wrong answers cleared!")
            st.experimental_rerun()
