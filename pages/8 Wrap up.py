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
    if "remaining_questions" not in st.session_state:
        st.session_state.remaining_questions = random.sample(questions_data, len(questions_data))
        st.session_state.score = 0
        st.session_state.current_question = None
        st.session_state.quiz_done = False
        st.session_state.answered = False
        st.session_state.feedback = ""
        st.session_state.user_answer = None
        st.session_state.question_index = 0  # 새로 추가됨

    # 퀴즈 완료 처리
    if st.session_state.quiz_done:
        st.success(f"✅ Quiz Complete! Your score: {st.session_state.score}/{len(questions_data)}")
        if st.button("Restart Quiz"):
            st.session_state.clear()
        return

    # 다음 질문 바로 설정
    if st.session_state.current_question is None:
        if st.session_state.question_index < len(questions_data):
            st.session_state.current_question = st.session_state.remaining_questions[st.session_state.question_index]
        else:
            st.session_state.quiz_done = True
            return

    q = st.session_state.current_question
    st.write(f"Question: {q['question']}")

    st.session_state.user_answer = st.radio("Choose one:", ("O", "X"), key=f"answer_{st.session_state.question_index}")

    # 정답 제출
    if not st.session_state.answered:
        if st.button("Submit Answer"):
            if st.session_state.user_answer == q["answer"]:
                st.session_state.score += 1
                st.session_state.feedback = "✅ Correct!"
            else:
                st.session_state.feedback = f"❌ Wrong! The correct answer was '{q['answer']}'."
            st.session_state.answered = True

    # 피드백 표시
    if st.session_state.feedback:
        st.info(st.session_state.feedback)

    # 다음 문제로 이동
    if st.session_state.answered:
        if st.button("Next Question"):
            st.session_state.question_index += 1
            if st.session_state.question_index < len(questions_data):
                st.session_state.current_question = None
                st.session_state.answered = False
                st.session_state.feedback = ""
                st.session_state.user_answer = None
            else:
                st.session_state.quiz_done = True

if __name__ == "__main__":
    quiz()
