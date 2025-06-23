import streamlit as st
import random

with st.expander("📘 How to Play / Instructions (Click to Expand)"):
    st.markdown("""
    ## 🧑‍🏫 Passive Voice Word Order Quiz Guide

    This app helps you **practice changing active voice sentences into passive voice** by arranging shuffled words in the correct order.

    ---

    ### 🟩 Instructions

    1. **Read the active sentence** at the top.  
       Example: `Tom eats an apple.`

    2. **Select the words** from the buttons below to form the correct passive sentence.  
       Example: `An apple is eaten by Tom`

    3. The words you select will appear under **📝 Your Sentence**.

    4. Use the buttons below to control your progress:
       - ✅ **Submit**: Check if your sentence is correct.
       - 🔄 **Clear**: Reset your selection and try again.
       - ⏭️ **Next**: Move to the next question *only after a correct answer*.

    5. Your current score is displayed under **📊 Score**.

    ---

    ### 📌 Notes

    - You can **only select each word once**.
    - You **must match the exact word order** to get the answer right.
    - You can’t move to the next question **unless your answer is correct**.

    ---

    ### 🎯 Learning Goal

    This quiz is designed to help you:
    - Understand how to construct passive voice sentences.
    - Practice English grammar in a fun and interactive way!
    """)


# 문제 은행
quiz_bank = [
    {
        "active": "Tom eats an apple.",
        "passive": ["An", "apple", "is", "eaten", "by", "Tom"]
    },
    {
        "active": "She cleans the room.",
        "passive": ["The", "room", "is", "cleaned", "by", "her"]
    },
    {
        "active": "They watch a movie.",
        "passive": ["A", "movie", "is", "watched", "by", "them"]
    },
    {
        "active": "He reads a book.",
        "passive": ["A", "book", "is", "read", "by", "him"]
    },
    {
        "active": "The dog bites the man.",
        "passive": ["The", "man", "is", "bitten", "by", "the", "dog"]
    }
]

# 상태 초기화
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'selected_words' not in st.session_state:
    st.session_state.selected_words = []
if 'used_words' not in st.session_state:
    st.session_state.used_words = []
if 'shuffled_words' not in st.session_state:
    st.session_state.shuffled_words = []
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'feedback_shown' not in st.session_state:
    st.session_state.feedback_shown = False

# 새 문제 로드
def load_question():
    question = quiz_bank[st.session_state.current_index]
    st.session_state.selected_words = []
    st.session_state.used_words = []
    st.session_state.feedback_shown = False
    st.session_state.shuffled_words = random.sample(question["passive"], len(question["passive"]))

# 단어 선택
def select_word(word):
    if word not in st.session_state.used_words:
        st.session_state.selected_words.append(word)
        st.session_state.used_words.append(word)

# 초기 문제 로딩
if not st.session_state.shuffled_words:
    load_question()

# UI
st.title("🔠 Passive Voice Word Order Quiz")
question = quiz_bank[st.session_state.current_index]
st.markdown(f"### ✅ Active Sentence:\n`{question['active']}`")

st.markdown("### 🔤 Arrange the Passive Sentence:")

# 선택 UI
cols = st.columns(5)
for idx, word in enumerate(st.session_state.shuffled_words):
    if word not in st.session_state.used_words:
        if cols[idx % 5].button(word, key=f"word_{idx}"):
            select_word(word)

# 선택된 단어 보기
st.markdown("**📝 Your Sentence:**")
st.markdown(" ".join(st.session_state.selected_words) or "`(No words selected yet)`")

# 버튼 조작 영역
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("✅ Submit"):
        if st.session_state.selected_words == question["passive"]:
            st.success("🎉 Correct!")
            st.session_state.score += 1
            st.session_state.feedback_shown = True
        else:
            st.error("❌ Incorrect. Try again.")

with col2:
    if st.button("🔄 Clear"):
        st.session_state.selected_words = []
        st.session_state.used_words = []

with col3:
    if st.button("⏭️ Next") and st.session_state.feedback_shown:
        st.session_state.current_index = (st.session_state.current_index + 1) % len(quiz_bank)
        load_question()

st.markdown(f"### 📊 Score: {st.session_state.score} / {len(quiz_bank)}")

