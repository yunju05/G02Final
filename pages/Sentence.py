import streamlit as st
import random

# 올바른 문장과 무작위로 섞인 단어 리스트를 준비합니다.
correct_sentence = ["This", "is", "a", "sample", "sentence"]
words = correct_sentence.copy()
random.shuffle(words)

# 상태를 위한 session state 초기화
if 'selected_words' not in st.session_state:
    st.session_state.selected_words = []

def select_word(word):
    st.session_state.selected_words.append(word)

def submit_answer():
    if st.session_state.selected_words == correct_sentence:
        st.success("Correct!")
    else:
        st.error("Incorrect. Try again!")

def clear_selection():
    st.session_state.selected_words = []

# Streamlit 인터페이스 설정
st.markdown("### Arrange the words in the correct order:")

# 각 단어에 대한 버튼 생성
for word in words:
    if st.button(word):
        select_word(word)

# 선택된 단어를 보여줍니다.
st.text("Selected Words: " + " ".join(st.session_state.selected_words))

# 제출 버튼과 초기화 버튼 생성
if st.button("Submit"):
    submit_answer()

if st.button("Clear"):
    clear_selection()
    # st.experimental_rerun() is removed, state is cleared without rerun.
