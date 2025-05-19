import streamlit as st
from PIL import Image

# 이미지 파일 경로
image_path = 'https://github.com/user-attachments/assets/3a4f3c17-aa5b-427a-a505-e6a1abfa493d'  # 이미지 파일이 있는 경로

# 이미지 열기
image = Image.open(image_path)

# 이미지 표시
st.image(image, caption='Your Image Caption', use_container_width=True)


print("Welcome to our High-Technology English class!")

