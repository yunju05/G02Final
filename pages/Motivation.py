import streamlit as st

st.write("Motivation")

tab1, tab2 = st.tabs([
    "1. Story Guessing ", 
    "2. Story Listening "])

######### TAB 1: Word List #########
with tab1:
    url="https://github.com/yunju05/G02Final/raw/main/images/%EB%94%94%EB%A6%AC%20text%20picture.png"
    st.image(url)
    url1="https://github.com/yunju05/G02Final/raw/main/images/%EB%94%94%EB%A6%AC%20%EC%9B%8C%EB%93%9C%20%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C.png"
    st.image(url1)
    st.write("Let's guessing the content of this story and share it!")

######### TAB 1: Word List #########
with tab2:
    st.write("Let's listening the story!")
