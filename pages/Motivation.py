import streamlit as st

st.write("Motivation")

    url="https://github.com/yunju05/G02Final/raw/main/images/%EB%94%94%EB%A6%AC%20text%20picture.png"
    st.image(url)
    url1="https://github.com/yunju05/G02Final/raw/main/images/%EB%94%94%EB%A6%AC%20%EC%9B%8C%EB%93%9C%20%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C.png"
    st.image(url1)
    st.write("Let's guessing the content of this story and share it!")
    if 'comments' not in st.session_state:
    st.session_state['comments'] = []
    def add_comment():
    comment_input = st.session_state['comment_input']
    if comment_input:
        if comment_input.strip().lower() == '댓글':
             st.session_state['comments'].clear()
        else:

    st.session_state['comments'].append(comment_input)
    st.session_state['comment_input'] = ''
    st.text_input("댓글을 입력하세요:", key='comment_input', on_change=add_comment)
    st.write("### 댓글 목록")
    for idx, comment in enumerate(st.session_state['comments']):
    st.write(f"{idx + 1}. {comment}")

