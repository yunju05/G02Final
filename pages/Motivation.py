import streamlit as st
url="https://github.com/yunju05/G02Final/raw/main/images/%EB%94%94%EB%A6%AC%20text%20picture.png"
st.image(url)
url1="https://github.com/yunju05/G02Final/raw/main/images/%EB%94%94%EB%A6%AC%20%EC%9B%8C%EB%93%9C%20%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C.png"
st.image(url1)

import streamlit as st

# 초기화: 세션 상태에 'comments'가 없으면 빈 리스트로 초기화
if 'comments' not in st.session_state:
    st.session_state['comments'] = []

# 댓글 입력을 위한 텍스트 입력 필드
comment_input = st.text_input("댓글을 입력하세요:")

# '댓글 남기기' 버튼
if st.button("댓글 남기기"):
    # 댓글이 비어있지 않으면 세션 상태에 추가
    if comment_input:
        st.session_state['comments'].append(comment_input)
        # 입력 필드를 초기화
        st.text_input("댓글을 입력하세요:", value='', key='comment_input')

# 저장된 댓글 표시
st.write("### 댓글 목록")
for idx, comment in enumerate(st.session_state['comments']):
    st.write(f"{idx + 1}. {comment}")

