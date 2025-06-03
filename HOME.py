from PIL import Image
import requests
from io import BytesIO
import streamlit as st

image_url = 'https://github.com/yunju05/G02Final/raw/main/images/app.png'
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

st.markdown("# Welcome to Our Digital English Class!")

# HTML로 이미지 크기 조절 (예: 가로 60%)
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="{image_url}" alt="GitHub Image" style="width:60%;">
        <p style="font-size: 16px; color: gray;">Digital class QR</p>
    </div>
    """,
    unsafe_allow_html=True
)

