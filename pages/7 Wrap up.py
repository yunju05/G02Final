import streamlit as st
import random

# 퀴즈 데이터
questions_data = [
    {
        "question": "Leo and his friends decided to explore the Whispering Woods because they were known for their beautiful scenery.",
        "answer": "X"
    },
    {
        "question": "The Whispering Woods were avoided by locals due to the belief that they were bewitched.",
        "answer": "O"
    },
    {
        "question": "As the group ventured deeper into the woods, they encountered trees that could talk and share stories.",
        "answer": "O"
    },
    {
        "question": "The trees only told stories about happy endings and celebrations.",
        "answer": "X"
    },
    {
        "question": "After leaving the woods, Leo and his friends felt a stronger commitment to protecting nature.",
        "answer": "O"
    }
]

def quiz():
    st.title("# ⭕✖️ Quiz on the Story")

    # 상태 초기화
    if "remaining_questions" not in st.session_state:
        st.session_state.remaining_questions = random.sample(questions_data, len(questions_data))
        st.session_state.score = 0
        st.session_state.current_question = None
        st.session_state.quiz_done = False
        st.session_state.answered = False
        st.session_state.feedback = ""

    # 퀴즈 완료 시
    if st.session_state.quiz_done:
