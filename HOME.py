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


st.markdown("""
## 📚 About This Class

Welcome to our **Digital English Class**!  
This is a smart learning space where we combine language learning with technology.  
Here, you’ll find interactive activities, games, and materials to help you improve your English skills — anytime, anywhere.

🔹 **How to start:**  
Simply scan the QR code above to enter the class homepage.  
Each section will guide you through different learning modules step-by-step.

💡 Don't forget to bookmark this page for future access. Let's make learning fun and engaging together!
""")
