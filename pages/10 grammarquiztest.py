import streamlit as st
import random

# 문제은행
quiz_bank = [
    {
        "active": "Tom eats an apple.",
        "passive": ["An", "apple", "is", "eaten", "by", "Tom"]
    },
    {
        "active": "She cleans the room.",
        "passive": ["The", "room", "is", "cleaned", "by", "She"]
    },
    {
        "active": "They watch a movie.",
        "passive": ["A", "movie", "is", "watched", "by", "They"]
    },
    {
        "active": "He reads a book.",
        "passive": ["A", "book", "is", "read", "by", "He"]
    },
    {
        "active": "The dog bites the man.",
        "passive": ["The", "man", "is", "bitten", "by", "The", "dog"]
    }
]

# 문제 로드 함수
def load_new_question():
    question = random.choice(quiz_bank)
    st.session_state.current_question = question
    st.session_state.user_sentence = []
    shuffled = question["passive"].copy()
    random.shuffle(shuffled)
    st.session_state.shuffled_buttons = shuffled

# 세션 초기화
if "current_question" not in st.session_state:
    load_new_question()

active_sentence = st.session_state.current_question["active"]
correct_passive = st.session_state.current_question["passive"]

# UI
st.title("수동태 퀴즈")
st.markdown(f"**능동태 문장:** {active_sentence}")
st.write("아래 단어 버튼을 눌러 수동태 문장을 완성해보세요.")

# 단어 선택 버튼들
cols = st.columns(len(st.session_state.shuffled_buttons))
for i, word in enumerate(st.session_state.shuffled_buttons):
    if cols[i].button(word, key=f"select_{i}_{word}"):
        st.session_state.user_sentence.append(word)

# 만든 문장 출력
st.markdown("#### 만든 문장:")
if st.session_state.user_sentence:
    delete_cols = st.columns(len(st.session_state.user_sentence))
    for i, word in enumerate(st.session_state.user_sentence):
        with delete_cols[i]:
            st.write(f"`{word}`")
            if st.button("❌", key=f"delete_{i}"):
                st.session

