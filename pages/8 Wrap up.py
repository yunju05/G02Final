import streamlit as st
import random

# 퀴즈 데이터 정의
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
    st.set_page_config(page_title="OX Quiz")
    st.title("⭕✖️ Quiz on the Story")

    # 초기 상태 설정
    if "shuffled_questions" not in st.session_state:
        st.session_state.shuffled_questions = random.sample(questions_data, len(questions_data))
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.feedback = ""
        st.session_state.user_answer = None
        st.session_state.quiz_done = False

    # 퀴즈 종료 처리
    if st.session_state.quiz_done:
        st.success(f"✅ Quiz Complete! Your score: {st.session_state.score}/{len(questions_data)}")
        if st.button("Restart Quiz"):
            st.session_state.clear()
        return

    # 현재 질문
    current_q = st.session_state.shuffled_questions[st.session_state.question_index]
    st.write(f"Question {st.session_state.question_index + 1}: {current_q['question']}")

    # 사용자 선택
    if not st.session_state.answered:
        st.session_state.user_answer = st.radio("Choose one:", ("O", "X"), key=f"q_{st.session_state.question_index}")
        if st.button("Submit Answer"):
            st.session_state.answered = True
            if st.session_state.user_answer == current_q["answer"]:
                st.session_state.score += 1
                st.session_state.feedback = "✅ Correct!"
            else:
                st.session_state.feedback = f"❌ Wrong! The correct answer was '{current_q['answer']}'."

    # 피드백 및 다음 버튼
    if st.session_state.answered:
        st.info(st.session_state.feedback)
        if st.button("Next Question"):
            st.session_state.question_index += 1
            if st.session_state.question_index >= len(st.session_state.shuffled_questions):
                st.session_state.quiz_done = True
            else:
                # 다음 문제로 넘어갈 준비
                st.session_state.answered = False
                st.session_state.feedback = ""
                st.session_state.user_answer = None

if __name__ == "__main__":
    quiz()
