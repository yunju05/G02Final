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

    # 세션 상태 초기화
    if "questions" not in st.session_state:
        st.session_state.questions = random.sample(questions_data, len(questions_data))
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.feedback = ""
        st.session_state.finished = False

    # 퀴즈 끝났을 경우
    if st.session_state.finished:
        st.success(f"🎉 Quiz Finished! Your score: {st.session_state.score}/{len(st.session_state.questions)}")
        if st.button("Restart Quiz"):
            st.session_state.clear()
        return

    # 현재 질문
    question = st.session_state.questions[st.session_state.q_index]
    st.write(f"Question {st.session_state.q_index + 1}: {question['question']}")

    # 답 선택
    if not st.session_state.answered:
        user_answer = st.radio("Choose one:", ("O", "X"), key=f"answer_{st.session_state.q_index}")
        if st.button("Submit Answer"):
            st.session_state.answered = True
            if user_answer == question["answer"]:
                st.session_state.score += 1
                st.session_state.feedback = "✅ Correct!"
            else:
                st.session_state.feedback = f"❌ Wrong! The correct answer was '{question['answer']}'."

    # 피드백 및 다음 버튼
    if st.session_state.answered:
        st.info(st.session_state.feedback)
        if st.button("Next Question"):
            st.session_state.q_index += 1
            if st.session_state.q_index >= len(st.session_state.questions):
                st.session_state.finished = True
            else:
                st.session_state.answered = False
                st.session_state.feedback = ""
                # 유저의 이전 선택 상태 초기화
                del st.session_state[f"answer_{st.session_state.q_index - 1}"]
            st.experimental_rerun()  # 여기서 정확하게 rerun을 걸어야 즉시 반영됨

if __name__ == "__main__":
    quiz()
