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
    st.title("⭕✖️ Quiz on the Story")

    if "remaining_questions" not in st.session_state:
        st.session_state.remaining_questions = random.sample(questions_data, len(questions_data))
        st.session_state.score = 0
        st.session_state.current_question = None
        st.session_state.quiz_done = False
        st.session_state.answered = False
        st.session_state.feedback = ""

    if st.session_state.quiz_done:
        st.success(f"✅ Quiz Complete! Your score: {st.session_state.score}/{len(questions_data)}")
        if st.session_state.score == len(questions_data):
            st.write("🎉 Excellent! You understood the story perfectly.")
        else:
            st.write("📖 Review the story and try again to improve your score.")
        if st.button("Restart Quiz"):
            st.session_state.clear()
        return

    if st.session_state.current_question is None and st.session_state.remaining_questions:
        st.session_state.current_question = st.session_state.remaining_questions.pop()
        st.session_state.answered = False
        st.session_state.feedback = ""

    q = st.session_state.current_question
    st.write(f"Question: {q['question']}")
    user_answer = st.radio("Choose one:", ("O", "X"), key=f"answer_{len(st.session_state.remaining_questions)}")

    if st.button("Submit Answer") and not st.session_state.answered:
        if user_answer == q["answer"]:
            st.session_state.score += 1
            st.session_state.feedback = "✅ Correct!"
        else:
            st.session_state.feedback = f"❌ Wrong! The correct answer was '{q['answer']}'."
        st.session_state.answered = True

    if st.session_state.feedback:
        st.info(st.session_state.feedback)

    if st.session_state.answered:
        if st.button("Next Question"):
            if st.session_state.remaining_questions:
                st.session_state.current_question = None
                st.session_state.answered = False
                st.session_state.feedback = ""
            else:
