import streamlit as st

# 능동태 문장과 정답 수동태 문장 설정
active_sentence = "Tom eats an apple."
correct_passive = ["An", "apple", "is", "eaten", "by", "Tom"]

st.title("수동태 퀴즈")
st.markdown("**능동태 문장:** Tom eats an apple.")
st.write("아래 단어 버튼을 눌러 수동태 문장을 완성해보세요.")

# 버튼 리스트
word_buttons = ["An", "apple", "is", "eaten", "by", "Tom"]

# 세션 상태 초기화
if "user_sentence" not in st.session_state:
    st.session_state.user_sentence = []

# 단어 버튼 출력
cols = st.columns(len(word_buttons))
for i, word in enumerate(word_buttons):
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

# 초기화 버튼
if st.button("초기화"):
    st.session_state.user_sentence = []
    st.experimental_rerun()
