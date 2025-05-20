import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# GitHub에 업로드된 이미지의 URL
image_url = 'https://github.com/yourusername/yourrepo/raw/main/path/to/your/image.jpg'

# URL에서 이미지 불러오기
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

# 큰 글씨로 텍스트 표시
st.markdown("# Welcome to our High-Technology English class!")

# 이미지 표시
st.image(image, caption='Image from GitHub', use_container_width=True)
