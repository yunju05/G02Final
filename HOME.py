import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.markdown("# Welcome to our High-Technology English class!")

# GitHub에 업로드된 이미지의 URL
image_url = 'https://github.com/user-attachments/assets/3a4f3c17-aa5b-427a-a505-e6a1abfa493d'

# URL에서 이미지 불러오기
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

# 이미지 표시 (크기 조절)
st.image(image, caption='QP for our app', width=400)  # 👈 크기를 줄임
