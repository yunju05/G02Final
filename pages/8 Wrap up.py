import streamlit as st

# 질문 데이터
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

# 상태 초기화
if 'q_index' not in st.session_state:
    st.session_state.q_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answered' not in st.session_state:
    st.session_state.answered = False

# 현재 문제 가져오기
current_question = questions_data[st.session_state.q_index]

st.title("🌲 Whispering Woods OX Quiz 🌲")
st.write(f"**Question {st.session_state.q_index + 1} of {len(questions_data)}**")
st.write(current_question["question"])

# 정답 버튼
col1, col2 = st.columns(2)
with col1:
    if st.button("O") and not st.session_state.answered:
        st.session_state.answered = True
        if current_question["answer"] == "O":
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error("❌ Incorrect!")
with col2:
    if st.button("X") and not st.session_state.answered:
        st.session_state.answered = True
        if current_question["answer"] == "X":
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error("❌ Incorrect!")

# 다음 문제로 넘어가기
if st.session_state.answered:
    if st.session_state.q_index < len(questions_data) - 1:
        if st.button("Next Question ➡️"):
            st.session_state.q_index += 1
            st.session_state.answered = False
    else:
        st.markdown("---")
        st.subheader("🎉 Quiz Complete!")
        st.write(f"Your final score: **{st.session_state.score} / {len(questions_data)}**")
        if st.button("Restart Quiz 🔄"):
            st.session_state.q_index = 0
            st.session_state.score = 0
            st.session_state.answered = False
