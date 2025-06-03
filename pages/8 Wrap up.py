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

def reset_quiz():
    st.session_state.remaining_questions = random.sample(questions_data, len(questions_data))
    st.session_state.score = 0
    st.session_state.current_question = None
    st.session_state.quiz_done = False
    st.session_state.answered = False
    st.session_state.feedback = ""
    st.session_state.user_answer = None

def quiz():
    st.set_page_config(page_title="OX Quiz")
    st.title("⭕✖️ Quiz on the Story")
    st.markdown("Test your understanding of the story with a quick OX quiz!")

    # 세션 상태 초기화
    if "remaining_questions" not in st.session_state:
        reset_quiz()

    # 퀴즈 완료
    if st.session_state.quiz_done:
        st.success(f"🎉 Quiz Complete! Your score: **{st.session_state.score}/{len(questions_data)}**")
        if st.button("🔁 Restart Quiz"):
            reset_quiz()
        return

    # 현재 문제 설정
    if st.session_state.current_question is None and st.session_state.remaining_questions:
        st.session_state.current_question = st.session_state.remaining_questions.pop()
        st.session_state.answered = False
        st.session_state.feedback = ""
        st.session_state.user_answer = None

    q = st.session_state.current_question
    st.subheader("📌 Question:")
    st.write(q["question"])

    # 사용자 선택
    if not st.session_state.answered:
        st.session_state.user_answer = st.radio(
            "Choose your answer:", 
            options=["O", "X"], 
            key=f"radio_{len(st.session_state.remaining_questions)}"
        )

        if st.button("✅ Submit Answer"):
            if st.session_state.user_answer == q["answer"]:
                st.session_state.score += 1
                st.session_state.feedback = "✅ Correct!"
            else:
                st.session_state.feedback = f"❌ Wrong! The correct answer was **'{q['answer']}'**."
            st.session_state.answered = True

    # 피드백
    if st.session_state.answered:
        st.info(st.session_state.feedback)

        if st.button("➡️ Next Question"):
            if st.session_state.remaining_questions:
                st.session_state.current_question = None
                st.session_state.answered = False
                st.session_state.feedback = ""
                st.session_state.user_answer = None
            else:
                st.session_state.quiz_done = True

if __name__ == "__main__":
    quiz()
