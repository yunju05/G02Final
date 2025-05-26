import streamlit as st
import requests

st.write("# 🍎 Warm up")


# 이미지 URL
url1 = "https://github.com/yunju05/G02Final/raw/main/images/%EB%94%94%EB%A6%AC%20text%20picture.png"
url2 = "https://github.com/yunju05/G02Final/raw/main/images/%EB%94%94%EB%A6%AC%20%EC%9B%8C%EB%93%9C%20%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C.png"

# 두 열로 나누기
col1, col2 = st.columns(2)

# 각 열에 이미지 표시
with col1:
    st.image(url1)

with col2:
    st.image(url2)

# 설명 텍스트
st.write("### Let's guess the content of this story and share it!")

st.subheader("📓 Guess Notebook")

# Initialize session state
if "guess_notes" not in st.session_state:
    st.session_state.guess_notes = []

# Form to add new guesses
with st.form("guess_form", clear_on_submit=True):
    new_guess = st.text_area("💭 Add a new guess:", height=100)
    submitted = st.form_submit_button("➕ Add")

    if submitted and new_guess.strip():
        st.session_state.guess_notes.append(new_guess.strip())
        st.success("Guess added!")

# Display saved guesses
st.markdown("---")
if st.session_state.guess_notes:
    for i, guess in enumerate(reversed(st.session_state.guess_notes), 1):
        st.markdown(f"**{len(st.session_state.guess_notes) - i + 1}.** {guess}")
else:
    st.info("No guesses yet. Start writing!")

# Clear guesses option
with st.expander("⚙️ Clear all guesses"):
    if st.button("🗑️ Delete All Guesses", key="delete_guesses"):
        st.session_state.guess_notes = []
        st.success("All guesses cleared.")

import streamlit as st

# 초기화: 세션 상태에 'comments'가 없으면 빈 리스트로 초기화
if 'comments' not in st.session_state:
    st.session_state['comments'] = []

# 콜백 함수 정의
def add_comment():
    comment_input = st.session_state['comment_input']
    if comment_input:
        if comment_input.strip().lower() == '댓글':
            # '댓글'이 입력되면 모든 댓글 삭제
            st.session_state['comments'].clear()
        else:
            # 새로운 댓글 추가
            st.session_state['comments'].append(comment_input)
        # 입력 필드를 초기화
        st.session_state['comment_input'] = ''

# 댓글 입력을 위한 텍스트 입력 필드
st.text_input("댓글을 입력하세요:", key='comment_input', on_change=add_comment)

# 저장된 댓글 표시
st.write("### 댓글 목록")
for idx, comment in enumerate(st.session_state['comments']):
    st.write(f"{idx + 1}. {comment}")
