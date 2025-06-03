import streamlit as st
import streamlit.components.v1 as components

st.write("# 🍎 Warm up")

url1 = "https://github.com/yunju05/G02Final/raw/main/images/%EB%94%94%EB%A6%AC%20text%20picture.png"
url2 = "https://github.com/yunju05/G02Final/raw/main/images/%EB%94%94%EB%A6%AC%20%EC%9B%8C%EB%93%9C%20%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C.png"

col1, col2 = st.columns(2)

with col1:
    st.image(url1)

with col2:
    st.image(url2)

st.write("### Let's guess the content of this story and share it!")

# Padlet 페이지를 iframe으로 임베드
padlet_url = "https://padlet.com/yunju05325/padlet-l9dikrb4yijjudux"

components.html(
    f'<iframe src="{padlet_url}" width="700" height="500" frameborder="0" allowfullscreen></iframe>',
    height=550,
)
