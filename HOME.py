import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# 이미지 파일 경로
image_path = 'https://github.com/user-attachments/assets/3a4f3c17-aa5b-427a-a505-e6a1abfa493d'  # 이미지 파일이 있는 경로
print("Welcome to our High-Technology English class!")

# GitHub에 업로드된 이미지의 URL
image_url = 'https://github.com/yunju05/G02Final/blob/main/images/app.png'

# 이미지 열기
image = Image.open(image_path)
# URL에서 이미지 불러오기
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

# 이미지 표시
st.image(image, caption='Your Image Caption', use_container_width=True)
st.image(image, caption='Image from GitHub', use_container_width=True)


print("Welcome to our High-Technology English class!")
