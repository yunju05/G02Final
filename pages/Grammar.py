import streamlit as st
import random
from gtts import gTTS
import os

# List of correct sentences
sentences = [
    ["Leo", "and", "his", "friends", "discovered", "a", "path", "leading", "to", "the", "Whispering", "Woods,", "known", "for", "the", "trees", "that", "could", "talk."],
    ["The", "locals", "avoided", "it,", "saying", "it", "was", "bewitched,", "but", "the", "adventurous", "teens", "couldn’t", "resist", "exploring."],
    ["As", "they", "walked", "deeper", "into", "the", "woods,", "the", "trees", "started", "whispering."],
    ["Each", "tree", "told", "stories", "of", "ancient", "times,", "of", "battles", "fought", "and", "lovers", "separated."],
    ["The", "trees", "also", "warned", "them", "about", "the", "dangers", "of", "forgetting", "the", "past", "and", "the", "importance", "of", "nature."],
    ["Moved", "by", "these", "stories,", "the", "friends", "promised", "to", "protect", "the", "woods", "and", "share", "their", "knowledge."],
    ["They", "left", "the", "woods", "wiser,", "with", "a", "deeper", "respect", "for", "nature", "and", "its", "untold", "stories,", "ready", "to", "advocate", "for", "its", "preservation."]
]

# Initialize session state
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
    play_tts()

def play_tts():
    # Get the current sentence as a string
    current_sentence = ' '.join(sentences[st.session_state.current_index])
    # Generate TTS audio
    tts = gTTS(current_sentence)
    tts.save("current_sentence.mp3")
    # Play audio in streamlit
    audio_file = open("current_sentence.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3")
    audio_file.close()
    os.remove("current_sentence.mp3")

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
        play_tts()
    else:
        st.balloons()
        st.session_state.quiz_started = False
    st.session_state.show_options = False

def clear_selection():
    st.session_state.selected_words = []

# Streamlit 인터페이스
if not st.session_state.quiz_started:
    st.button("Start Quiz", on_click=start_quiz)
else:
    # 현재 문장과 섞인 단어들
    correct_sentence = sentences[st.session_state.current_index]
    words = correct_sentence.copy()
    random.shuffle(words)

    st.markdown("### Arrange the words in the correct order:")

    # 아직 선택되지 않은 각 단어에 대해 버튼 생성
    for index, word in enumerate(words):
        if word not in st.session_state.selected_words:
            if st.button(word, key=f"{word}_{index}"):  # 각 버튼에 고유 키 추가
                select_word(word)

    # 선택된 단어 표시
    st.markdown("### Selected Words:")
    st.markdown(f"**{' '.join(st.session_state.selected_words)}**")

    # 제출 및 초기화 버튼 생성
    if st.button("Submit"):
        submit_answer()

    if st.button("Clear"):
        clear_selection()

    # 정답을 맞춘 후 재시도 및 다음 버튼 표시
    if 'show_options' in st.session_state and st.session_state.show_options:
        st.button("Retry", on_click=retry)
        st.button("Next", on_click=next_problem)
