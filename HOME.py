import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# GitHub URL에서 이미지 불러오기
image_url = 'https://github.com/user-attachments/assets/3a4f3c17-aa5b-427a-a505-e6a1abfa493d'
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

# 이미지 표시
st.image(image, caption='Your Image Caption', use_column_width=True)

print("Welcome to our High-Technology English class!")

