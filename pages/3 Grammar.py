import streamlit as st

st.title("Grammar")

# 탭 4개 만들기
tab1, tab2 = st.tabs(["Passive Voice", "동명사"])

with tab1:
    st.header("🧠 What is Passive Voice?")
    st.markdown("Write here.")
 

with tab2:
    st.header("🔁 동명사 탭 내용 작성하세요")
    st.markdown("Write here.")
