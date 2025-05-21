import streamlit as st

def quiz():
    st.title("# ⭕✖️ Quiz on the Story")

    questions = [
        "Leo and his friends decided to explore the Whispering Woods because they were known for their beautiful scenery.",
        "The Whispering Woods were avoided by locals due to the belief that they were bewitched.",
        "As the group ventured deeper into the woods, they encountered trees that could talk and share stories.",
        "The trees only told stories about happy endings and celebrations.",
        "After leaving the woods, Leo and his friends felt a stronger commitment to protecting nature."
    ]

    answers = ['X', 'O', 'O', 'X', 'O']
    user_answers = []

    for i, question in enumerate(questions):
        st.write(f"Question {i+1}: {question}")
        user_answer = st.radio("", ("O", "X"), key=f"question_{i}")
        user_answers.append(user_answer)

    if st.button("Submit Answers"):
        score = 0
        for i, user_answer in enumerate(user_answers):
            if user_answer == answers[i]:
                score += 1

        st.write(f"Your score: {score}/{len(questions)}")
        if score == len(questions):
            st.write("Excellent! You understood the story perfectly.")
        else:
            st.write("Review the story and try again to improve your score.")

if __name__ == "__main__":
    quiz()

