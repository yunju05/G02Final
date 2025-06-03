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

# 하이퍼링크 만들기
st.markdown("[Visit Padlat](https://padlet.com/yunju05325/padlet-l9dikrb4yijjudux)")

