import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO
import random

st.write("⭐ Vocabulary learning")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "1. Lesson: Word list", 
    "2. Activity: Listen to the word", 
    "3. Spelling practice", 
    "4. Quiz: Korean meaning → English", 
    "5. Review: Mistakes"
])

# Load CSV once at the start to avoid repetition
@st.cache_data
def load_data():
    url = "https://github.com/yunju05/G02Final/raw/main/data/word.csv"
    df = pd.read_csv(url)
    df = df.dropna(subset=["Word", "Meaning"])  # 단어, 뜻 없는 행 제거
    return df

df = load_data()
word_list = df["Word"].tolist()
meaning_list = df["Meaning"].tolist()

# Initialize session state keys if missing
if "current_word" not in st.session_state:
    st.session_state.current_word = None
if "audio_data" not in st.session_state:
    st.session_state.audio_data = None
if "check_clicked" not in st.session_state:
    st.session_state.check_clicked = False
if "quiz_current_idx" not in st.session_state:
    st.session_state.quiz_current_idx = None
if "quiz_input" not in st.session_state:
    st.session_state.quiz_input = ""
if "quiz_check_clicked" not in st.session_state:
    st.session_state.quiz_check_clicked = False
if "mistakes" not in st.session_state:
    st.session_state.mistakes = []  # 틀린 단어 리스트, 중복 허용 안 함

######### TAB 1: Word List #########
with tab1:
    st.markdown("### 🔠 Word and Expression")
    if st.button("Show Word List"):
        st.dataframe(df, use_container_width=True)

######### TAB 2: Listen to word #########
with tab2:
    st.title("🎧 Word Pronunciation Practice")
    selected_word = st.selectbox("Choose a word to hear:", word_list)

    if selected_word:
        tts = gTTS(selected_word, lang='en')
        audio_fp = BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        st.audio(audio_fp, format='audio/mp3')

######### TAB 3: Spelling Practice #########
with tab3:
    st.markdown("### 🎧 Listen and Type the Word")
    st.caption("Click the button to hear a word. Then type it and press 'Check the answer'.")

    if st.button("🔊 Let me listen to a word"):
        st.session_state.current_word = random.choice(word_list)
        st.session_state.check_clicked = False
        st.session_state.user_input = ""  # 초기화

        tts = gTTS(st.session_state.current_word, lang='en')
        audio_fp = BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        st.session_state.audio_data = audio_fp.read()

    if st.session_state.audio_data:
        st.audio(st.session_state.audio_data, format='audio/mp3')

    user_input = st.text_input("Type the word you heard:", key="user_input")

    if st.button("✅ Check the answer"):
        st.session_state.check_clicked = True

        if st.session_state.current_word:  # 답이 있는 경우에만 체크
            if user_input.strip().lower() == st.session_state.current_word.lower():
                st.success("✅ Correct!")
                # 맞췄으면 틀린 단어 리스트에서 제거 (있으면)
                if st.session_state.current_word in st.session_state.mistakes:
                    st.session_state.mistakes.remove(st.session_state.current_word)
            else:
                st.error(f"❌ Try again. Correct answer: {st.session_state.current_word}")
                # 틀린 단어는 중복 없이 저장
                if st.session_state.current_word not in st.session_state.mistakes:
                    st.session_state.mistakes.append(st.session_state.current_word)

######### TAB 4: Quiz (Meaning → English) #########

def check_quiz_answer():
    answer_stripped = st.session_state.quiz_input.strip()
    correct_word = df.iloc[st.session_state.quiz_current_idx]["Word"]

    if answer_stripped.lower() == correct_word.lower():
        st.session_state.quiz_feedback = "correct"
        if correct_word in st.session_state.mistakes:
            st.session_state.mistakes.remove(correct_word)
    else:
        st.session_state.quiz_feedback = f"wrong: 정답은 '{correct_word}' 입니다."
        if correct_word not in st.session_state.mistakes:
            st.session_state.mistakes.append(correct_word)

    # 다음 문제로 넘어가기
    st.session_state.quiz_current_idx = random.randint(0, len(df)-1)
    st.session_state.quiz_input = ""

# 초기 상태 변수
if "quiz_feedback" not in st.session_state:
    st.session_state.quiz_feedback = ""

with tab4:
    st.markdown("### 📝 Write the English word from the Korean meaning")

    if st.session_state.quiz_current_idx is None:
        st.session_state.quiz_current_idx = random.randint(0, len(df)-1)
        st.session_state.quiz_input = ""
        st.session_state.quiz_feedback = ""

    meaning = df.iloc[st.session_state.quiz_current_idx]["Meaning"]

    st.write(f"**Korean meaning:** {meaning}")

    st.text_input("Your answer:", key="quiz_input", on_change=check_quiz_answer)

    if st.session_state.quiz_feedback == "correct":
        st.success("✅ Correct! 다음 문제로 넘어갑니다.")
    elif st.session_state.quiz_feedback.startswith("wrong"):
        st.error(st.session_state.quiz_feedback.split(": ")[1])



######### TAB 5: Review Mistakes #########
with tab5:
    st.markdown("### 🔄 Review your mistakes")

    if len(st.session_state.mistakes) == 0:
        st.info("You have no mistakes to review! 🎉")
    else:
        mistake_word = random.choice(st.session_state.mistakes)
        mistake_meaning = df.loc[df["Word"] == mistake_word, "Meaning"].values[0]

        st.write(f"**Korean meaning:** {mistake_meaning}")

        review_input = st.text_input("Write the English word:", key="review_input")

        if st.button("Check answer for review"):
            if review_input.strip().lower() == mistake_word.lower():
                st.success("✅ Correct! Removed from mistakes.")
                st.session_state.mistakes.remove(mistake_word)
            else:
                st.error(f"❌ Incorrect! The correct word is '{mistake_word}'.")
