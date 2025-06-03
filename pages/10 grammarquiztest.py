import streamlit as st
import random

# 능동태 문장과 정답 수동태 문장 설정
active_sentence = "Tom eats an apple."
correct_passive = ["An", "apple", "is", "eaten", "by", "Tom"]

st.title("수동태 퀴즈")
st.markdown("**능동태 문장:** Tom eats an apple.")
st.write("아래 단어 버튼을 눌러 수동태 문장을 완성해보세요.")

# 버튼 리스트 (정답용은 따로 유지)
base_buttons = ["An", "apple", "is", "eaten", "by", "Tom"]

# 버튼 순서를 한 번만 섞도록 세션 상태에 저장
if "shuffled_buttons" not in st.session_state:
    st.session_state.shuffled_buttons = base_buttons.copy()
    random.shuffle(st.session_state.shuffled_buttons)

# 사용자 입력 초기화
if "user_sentence" not in st.session_state:
    st.session_state.user_sentence = []

# 섞인 순서로 버튼 출력
cols = st.columns(len(base_buttons))
for i, word in enumerate(st.session_state.shuffled_buttons):
    if cols[i].button(word, key=f"btn_{i}"):
        st.session_state.user_sentence.append(word)

# 현재 문장 출력
user_sentence = st.session_state.user_sentence
st.markdown("#### 만든 문장:")
st.write(" ".join(user_sentence))

# 제출 버튼
if st.button("제출"):
    if user_sentence == correct_passive:
        st.success("정답입니다! 🎉")
    else:
        st.error("틀렸어요. 다시 시도해보세요.")

# 초기화 버튼 (버튼 순서도 다시 섞임)
if st.button("초기화"):
    st.session_state.user_sentence = []
    st.session_state.shuffled_buttons = base_buttons.copy()
    random.shuffle(st.session_state.shuffled_buttons)
    st.experimental_rerun()
