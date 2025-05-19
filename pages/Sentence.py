import streamlit as st
import random

# Correct sentence
correct_sentence = ["This", "is", "a", "sample", "sentence"]

# Initialize session state for words
if 'words' not in st.session_state:
    st.session_state.words = correct_sentence.copy()
    random.shuffle(st.session_state.words)

# Initialize session state for selected words
if 'selected_words' not in st.session_state:
    st.session_state.selected_words = []

def select_word(word):
    st.session_state.selected_words.append(word)

def submit_answer():
    if st.session_state.selected_words == correct_sentence:
        st.success("Correct!")
    else:
        st.error("Incorrect. Try again!")

def clear_selection():
    st.session_state.selected_words = []

# Streamlit interface
st.markdown("### Arrange the words in the correct order:")

# Create buttons for each word
for word in st.session_state.words:
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
