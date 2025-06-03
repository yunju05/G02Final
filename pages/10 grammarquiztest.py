import streamlit as st
import random

# 문제은행: 능동태 → 수동태 정답 리스트
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

# 함수: 문제 초기화
def load_new_question():
    question = random.choice(quiz_bank)
    st.session_state.current_question = question
    st.session_state.user_sentence = []
    shuffled = question["passive"].copy()
    random.shuffle(shuffled)
    st.session_state.shuffled_buttons = shuffled

# 세션 상태 초기화
if "current_question" not in st.session_state:
    load_new_question()

# 문제 정보
active_sentence = st.session_state.current_question["active"]
correct_passive = st.session_state.current_question["passive"]

# 제목
st.title("수동태 퀴즈")
st.markdown(f"**능동태 문장:** {active_sentence}")
st.write("아래 단어 버튼을 눌러 수동태 문장을 완성해보세요.")

# 버튼 UI
cols = st.columns(len(st.session_state.shuffled_buttons))
for i, word in enumerate(st.session_state.shuffled_buttons):
    if cols[i].button(word, key=f"btn_{i}_{word}"):
        st.session_state.user_sentence.append(word)

# 만든 문장 출력
st.markdown("#### 만든 문장:")
st.write(" ".join(st.session_state.user_sentence))

# 제출
if st.button("제출"):
    if st.session_state.user_sentence == correct_passive:
        st.success("정답입니다! 🎉")
    else:
        st.error("틀렸어요. 다시 시도해보세요.")

# 새 문제 로딩 (rerun 없이)
if st.button("새 문제"):
    load_new_question()
