import streamlit as st
import random

# List of correct sentences
sentences = [
    ["This", "is", "a", "sample", "sentence"],
    ["Streamlit", "makes", "apps", "easy", "to", "build"],
    ["Python", "is", "a", "versatile", "language"],
    ["Data", "science", "is", "an", "exciting", "field"]
]

# Initialize session state
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'selected_words' not in st.session_state:
    st.session_state.selected_words = []
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False

def start_quiz():
    st.session_state.quiz_started = True
    st.session_state.current_index = 0
    st.session_state.selected_words = []

def select_word(word):
    st.session_state.selected_words.append(word)

def submit_answer():
    if st.session_state.selected_words == sentences[st.session_state.current_index]:
        st.success("Correct!")
        st.session_state.show_options = True
    else:
        st.error("Incorrect. Try again!")

def retry():
    st.session_state.selected_words = []

def next_problem():
    if st.session_state.current_index < len(sentences) - 1:
        st.session_state.current_index += 1
        st.session_state.selected_words = []
    else:
        st.balloons()
        st.session_state.quiz_started = False
    st.session_state.show_options = False

def clear_selection():
    st.session_state.selected_words = []

# Streamlit interface
if not st.session_state.quiz_started:
    st.button("Start Quiz", on_click=start_quiz)
else:
    # Current sentence and shuffled words
    correct_sentence = sentences[st.session_state.current_index]
    words = correct_sentence.copy()
    random.shuffle(words)

    st.markdown("### Arrange the words in the correct order:")

    # Create buttons for each word that is not yet selected
    for word in words:
        if word not in st.session_state.selected_words:
            if st.button(word):
                select_word(word)

    # Display selected words with enhanced visibility
    st.markdown("### Selected Words:")
    st.markdown(f"**{' '.join(st.session_state.selected_words)}**")

    # Create submit and clear buttons
    if st.button("Submit"):
        submit_answer()

    if st.button("Clear"):
        clear_selection()

    # Show retry and next buttons after a correct answer
    if 'show_options' in st.session_state and st.session_state.show_options:
        st.button("Retry", on_click=retry)
        st.button("Next", on_click=next_problem)
