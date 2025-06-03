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

# 문제 로드 함수
def load_new_question():
    question = random.choice(quiz_bank)
    st.session_state.current_question = question
    st.session_state.user_sentence = []
    shuffled = question["passive"].copy()
    random.shuffle(shuffled)
    st.session_state.shuffled_buttons = shuffled

# 세션 상태 점검 및 초기화
if "current_question" not in st.session_state or st.session_state.current_question is None:
    load_new_question()

if "user_sentence" not in st.session_state:
    st.session_state.user_sentence = []

if "shuffled_buttons" not in st.session_state:
    st.session_state.shuffled_buttons = st.session_state.current_question["passive"].copy()
    random.shuffle(st.session_state.shuffled_buttons)

# 현재 문제 정보
question_data = st.session_state.current_question
active_sentence = question_data.get("active", "문제가 없습니다.")
correct_passive = question_data.get("passive", [])

# UI 출력
st.title("수동태 퀴즈")
st.markdown(f"**능동태 문장:** {active_sentence}")
st.write("아래 단어 버튼을 눌러 수동태 문장을 완성해보세요.")

# 단어 선택 버튼
cols = st.columns(len(st.session_state.shuffled_buttons))
for i, word in enumerate(st.session_state.shuffled_buttons):
    if cols[i].button(word, key=f"select_{i}_{word}"):
        st.session_state.user_sentence.append(word)

# 선택된 단어 출력 + 개별 삭제
st.markdown("#### 만든 문장:")
if st.session_state.user_sentence:
    for i, word in enumerate(st.session_state.user_sentence):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"`{word}`")
        with col2:
            # 삭제 요청을 감지하는 고유 버튼 키 사용
            if st.button("❌", key=f"del_{i}_{word}"):
                st.session_state.user_sentence.pop(i)
                # rerun 없이 로직 중단 (이후 루프 안 돌게)
                st.stop()
else:
    st.write("단어를 선택해보세요!")

# 정답 제출
if st.button("제출"):
    if st.session_state.user_sentence == correct_passive:
        st.success("정답입니다! 🎉")
    else:
        st.error("틀렸어요. 다시 시도해보세요.")

# 새 문제
if st.button("새 문제"):
    load_new_question()
