import streamlit as st
import pandas as pd
import numpy as np
from gtts import gTTS
from io import BytesIO
import random

st.write("⭐ Vocabulary learning")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "1. 📋Word list", 
    "2. 🔈Listen to the word", 
    "3. ✏️Spelling practice", 
    "4. 🔎Quiz", 
    "5. 🧩Crossword"
])

# Load CSV once at the start to avoid repetition
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/yunju05/G02Final/refs/heads/main/data/word.csv"
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
    st.session_state.mistakes = []  # Wrong words list. Disallow duplicate values 

######### TAB 1: 📋Word List #########
with tab1:
    st.markdown("### 🔠 Word and Expression")
    st.markdown("Here are 40 words from the lesson and some basic words you need to know.")
    if st.button("Show Word List"):
        st.dataframe(df, use_container_width=True)
    st.markdown("If you have learned all the words well, go to 🔈 page!")

######### TAB 2: 🔈Listen to word #########
with tab2:
    st.title("🎧 Word Pronunciation Practice")
    st.markdown("Choose a word you want, listen to the pronunciation, and try to say it!")
    
    selected_word = st.selectbox("Choose a word to hear:", word_list)

    if selected_word:
        tts = gTTS(selected_word, lang='en')
        audio_fp = BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        st.audio(audio_fp, format='audio/mp3')
    st.markdown("Did you practice the pronunciation enough? If yes, go to ✏️ page!")

######### TAB 3: ✏️Spelling Practice #########
with tab3:
    st.markdown("### 🎧 Listen and Type the Word")
    st.markdown("Now listen to the word in the audio and try to write the spelling!")
    st.caption("Click the button to hear a word. Then type it and press 'Check the answer'.")

    if st.button("🔊 Let me listen to a word"):
        st.session_state.current_word = random.choice(word_list)
        st.session_state.check_clicked = False
        st.session_state.user_input = ""  # Reset

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
        
        if st.session_state.current_word:  
            if user_input.strip().lower() == st.session_state.current_word.lower():
                st.success("✅ Correct!")
                # If the guessed word is correct, remove it from the wrong word list (if it exists)
                if st.session_state.current_word in st.session_state.mistakes:
                    st.session_state.mistakes.remove(st.session_state.current_word)
            else:
                st.error(f"❌ Try again. Correct answer: {st.session_state.current_word}")
                # Store incorrect words without duplicates
                if st.session_state.current_word not in st.session_state.mistakes:
                    st.session_state.mistakes.append(st.session_state.current_word)
    st.markdown("Great job! Now, shall we go to 🔎page?")
                
######### TAB 4: 🔎Quiz (Meaning → English) #########

# 초기 상태 변수 설정
if "quiz_current_idx" not in st.session_state:
    st.session_state.quiz_current_idx = None
if "quiz_input" not in st.session_state:
    st.session_state.quiz_input = ""
if "quiz_feedback" not in st.session_state:
    st.session_state.quiz_feedback = ""
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "quiz_total" not in st.session_state:
    st.session_state.quiz_total = 0

# 정답 확인 함수
def check_quiz_answer():
    answer_stripped = st.session_state.quiz_input.strip()
    correct_word = df.iloc[st.session_state.quiz_current_idx]["Word"]

    st.session_state.quiz_total += 1  # 시도 수 증가

    if answer_stripped.lower() == correct_word.lower():
        st.session_state.quiz_feedback = "correct"
        st.session_state.quiz_score += 1  # 정답이면 점수 증가
        if correct_word in st.session_state.mistakes:
            st.session_state.mistakes.remove(correct_word)
    else:
        st.session_state.quiz_feedback = f"wrong: The correct answer is '{correct_word}'."
        if correct_word not in st.session_state.mistakes:
            st.session_state.mistakes.append(correct_word)

    # 다음 문제로 이동
    st.session_state.quiz_current_idx = random.randint(0, len(df)-1)
    st.session_state.quiz_input = ""

# TAB 4: 퀴즈 화면
with tab4:
    st.markdown("### 📝 Write the English word from the Korean meaning")
    st.markdown("Look at the Korean meaning and write the English word!")

    
    st.write(f"**📊 Your Score:** {st.session_state.quiz_score} / {st.session_state.quiz_total}")

    if st.session_state.quiz_current_idx is None:
        st.session_state.quiz_current_idx = random.randint(0, len(df)-1)
        st.session_state.quiz_input = ""
        st.session_state.quiz_feedback = ""

    meaning = df.iloc[st.session_state.quiz_current_idx]["Meaning"]
    st.write(f"**Korean meaning:** {meaning}")

    st.text_input("Your answer:", key="quiz_input", on_change=check_quiz_answer)

    if st.session_state.quiz_feedback == "correct":
        st.success("✅ Correct! Let's move on to the next question.")
    elif st.session_state.quiz_feedback.startswith("wrong"):
        st.error(st.session_state.quiz_feedback.split(": ")[1])
    st.markdown("Did you get a good score? Then let’s go to the final page!")

######### TAB 5: Crossword #########


with tab5:
    st.title("📘 Crossword Puzzle")

    st.markdown("""
    Let's solve a crossword puzzle using the words you've learned from the story.  
    Look at the image below and try to guess the words using the definitions provided.
    You can download the image by right-clicking with your mouth or touchpad.
    """)

    # 퍼즐 이미지 불러오기 (문제 이미지)
    st.image(
        "https://github.com/yunju05/G02Final/raw/main/images/%ED%81%AC%EB%A1%9C%EC%8A%A4%EC%9B%8C%EB%93%9C.png", 
        caption: "🧩 Crossword Puzzle"
    )


    st.subheader("📝 Definitions")

    st.markdown("""
    **Down**  
    1. Controlled or enchanted by magical powers  
    2. The presence of harmful substances in the environment  
    3. Divided or moved apart from something or someone  
    4. To keep someone or something safe from harm or damage  
    5. To stay away from something or prevent it from happening

    **Across**  
    3. A work of art made by shaping stone, wood, or other materials  
    6. A feeling of deep admiration for someone or something  
    7. A state of physical ease and freedom from pain or stress  
    8. A small forest or an area covered with trees  
    9. The natural world including plants, animals, and landscapes
    """)

    # 정답 이미지 보기 버튼
    if st.button("👀 Show Answers"):
        st.image(
            "https://github.com/yunju05/G02Final/raw/main/images/%ED%81%AC%EB%A1%9C%EC%8A%A4%EC%9B%8C%EB%93%9C%20%EB%8B%B5.png",
            caption="✅ Crossword Answers"
        )
