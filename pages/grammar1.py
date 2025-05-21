import streamlit as st
import random
from gtts import gTTS
import os

sentences = [
    ["Leo", "and", "his", "friends", "discovered", "a", "path", "leading", "to", "the", "Whispering", "Woods", ",", "known", "for", "the", "trees", "that", "could", "talk"],
    ["The", "locals", "avoided", "it,", "saying", "it", "was", "bewitched", ",", "but", "the", "adventurous", "teens", "couldn’t", "resist", "exploring"],
    ["As", "they", "walked", "deeper", "into", "the", "woods", ",", "the", "trees", "started", "whispering"],
    ["Each", "tree", "told", "stories", "of", "ancient", "times", ",", "of", "battles", "fought", "and", "lovers", "separated"],
    ["The", "trees", "also", "warned", "them", "about", "the", "dangers", "of", "forgetting", "the", "past", "and", "the", "importance", "of", "nature"],
    ["Moved", "by", "these", "stories,", "the", "friends", "promised", "to", "protect", "the", "woods", "and", "share", "their", "knowledge"],
    ["They", "left", "the", "woods", "wiser,", "with", "a", "deeper", "respect", "for", "nature", "and", "its", "untold", "stories", ",", "ready", "to", "advocate", "for", "its", "preservation"]
]

if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'selected_words' not in st.session_state:
    st.session_state.selected_words = []
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'show_options' not in st.session_state:
    st.session_state.show_options = False

def start_quiz():
    st.session_state.quiz_started = True
    st.session_state.current_index = 0
    st.session_state.selected_words = []

def play_tts():
    current_sentence = ' '.join(sentences[st.session_state.current_index])
    tts = gTTS(current_sentence)
    tts.save("current_sentence.mp3")
    with open("current_sentence.mp3", "rb") as audio_file:
        audio_bytes = audio_file.read()
    os.remove("current_sentence.mp3")
    return audio_bytes

def select_word(word):
    st.session_state.selected_words.append(word)

def submit_answer():
    if st.session_state.selected_words == sentences[st.session_state.current_index]:
        st.success("Correct! Good job.")
        st.session_state.show_options = True
    else:
        st.error("Incorrect. Try rearranging the words again.")

def retry():
    st.session_state.selected_words = []

def next_problem():
    if st.session_state.current_index < len(sentences) - 1:
        st.session_state.current_index += 1
        st.session_state.selected_words = []
    else:
        st.success("Congratulations! You completed all the questions.")
        st.balloons()
        st.session_state.quiz_started = False
    st.session_state.show_options = False

def clear_selection():
    st.session_state.selected_words = []

st.title("Sentence Ordering Quiz")

if not st.session_state.quiz_started:
    st.write("Click 'Start Quiz' to begin. Listen to the sentence and arrange the words in the correct order.")
    st.button("Start Quiz", on_click=start_quiz)
else:
    audio_bytes = play_tts()
    st.audio(audio_bytes, format="audio/mp3")

    correct_sentence = sentences[st.session_state.current_index]
    words = correct_sentence.copy()
    random.shuffle(words)

    st.subheader(f"Question {st.session_state.current_index + 1}")
    st.write("Listen carefully, then arrange the words:")

    num_cols = 5
    cols = st.columns(num_cols)
    for idx, word in enumerate(words):
        if word not in st.session_state.selected_words:
            col_idx = idx % num_cols
            if cols[col_idx].button(word, key=f"{word}_{idx}"):
                select_word(word)

    st.markdown("**Your Answer:**")
    st.markdown(' '.join(st.session_state.selected_words))

    col1, col2 = st.columns(2)
    with col1:
        st.button("Submit", on_click=submit_answer)
    with col2:
        st.button("Clear", on_click=clear_selection)

    if st.session_state.show_options:
        col3, col4 = st.columns(2)
        with col3:
            st.button("Retry", on_click=retry)
        with col4:
            st.button("Next", on_click=next_problem)
