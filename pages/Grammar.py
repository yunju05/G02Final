import streamlit as st
import random

# Correct sentence and shuffled words
correct_sentence = ["This", "is", "a", "sample", "sentence"]
words = correct_sentence.copy()
random.shuffle(words)

# Initialize session state
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
