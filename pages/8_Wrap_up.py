import streamlit as st

questions_data = [
    {"question": "Leo and his friends decided to explore the Whispering Woods because they were known for their beautiful scenery.", "answer": "X"},
    {"question": "The Whispering Woods were avoided by locals due to the belief that they were bewitched.", "answer": "O"},
    {"question": "As the group ventured deeper into the woods, they encountered trees that could talk and share stories.", "answer": "O"},
    {"question": "The trees only told stories about happy endings and celebrations.", "answer": "X"},
    {"question": "After leaving the woods, Leo and his friends felt a stronger commitment to protecting nature.", "answer": "O"}
]

if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "user_answers" not in st.session_state:
    st.session_state.user_answers = []

def submit_answer(answer):
    st.session_state.user_answers.append(answer)
    st.session_state.q_index += 1

st.title("🌲 Whispering Woods OX Quiz 🌲")

if st.session_state.q_index < len(questions_data):
    q = questions_data[st.session_state.q_index]
    st.write(f"**Question {st.session_state.q_index + 1} of {len(questions_data)}**")
    st.write(q["question"])

    col1, col2 = st.columns(2)
    with col1:
        st.button("O", on_click=submit_answer, args=("O",), key=f"O_{st.session_state.q_index}")
    with col2:
        st.button("X", on_click=submit_answer, args=("X",), key=f"X_{st.session_state.q_index}")
else:
    st.subheader("🎉 Quiz Complete!")
    score = 0
    for i, q in enumerate(questions_data):
        user = st.session_state.user_answers[i]
        correct = q["answer"]
        result = "✅ Correct" if user == correct else "❌ Incorrect"
        if user == correct:
            score += 1
        st.markdown(
            f"""**Q{i+1}: {q['question']}**  
Your answer: {user} | Correct answer: {correct} → {result}"""
        )

    st.success(f"Total Score: {score} / {len(questions_data)}")

    if st.button("🔄 Restart Quiz"):
        st.session_state.q_index = 0
        st.session_state.user_answers = []
        # rerun 없이도 정상 작동
