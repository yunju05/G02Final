import streamlit as st
import random
from gtts import gTTS
import os

# 문장 및 중요 단어 인덱스
sentences = [
    ["Leo", "and", "his", "friends", "discovered", "a", "path", "leading", "to", "the", "Whispering", "Woods", ",", "known", "for", "the", "trees", "that", "could", "talk"],
    ["The", "locals", "avoided", "it,", "saying", "it", "was", "bewitched", ",", "but", "the", "adventurous", "teens", "couldn’t", "resist", "exploring"],
    ["As", "they", "walked", "deeper", "into", "the", "woods", ",", "the", "trees", "started", "whispering"],
    ["Each", "tree", "told", "stories", "of", "ancient", "times", ",", "of", "battles", "fought", "and", "lovers", "separated"],
    ["The", "trees", "also", "warned", "them", "about", "the", "dangers", "of", "forgetting", "the", "past", "and", "the", "importance", "of", "nature"],
    ["Moved", "by", "these", "stories,", "the", "friends", "promised", "to", "protect", "the", "woods", "and", "share", "their", "knowledge"],
    ["They", "left", "the", "woods", "wiser", ",", "with", "a", "deeper", "respect", "for", "nature", "and", "its", "untold", "stories", ",", "ready", "to", "advocate", "for", "its", "preservation"]
]
important_indices = [
    [4, 6, 7, 10, 17, 18, 19],
    [2, 6, 7, 13, 14, 15],
    [2, 3, 10, 11],
    [2, 3, 9, 10, 12, 13],
    [2, 3, 4, 7, 8, 9],
    [1, 2, 3, 4, 7, 8, 9, 13],
    [4, 8, 9, 13, 14, 15, 17, 18, 23]
]

# 상태 초기화
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'selected_words' not in st.session_state:
    st.session_state.selected_words = []
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'shuffled_words' not in st.session_state:
    st.session_state.shuffled_words = []
if 'used_words' not in st.session_state:
    st.session_state.used_words = []
if 'score' not in st.session_state:
    st.session_state.score = 0

# TTS 함수
def play_tts():
    current_sentence = ' '.join(sentences[st.session_state.current_index])
    tts = gTTS(current_sentence)
    tts.save("current_sentence.mp3")
    with open("current_sentence.mp3", "rb") as audio_file:
        audio_bytes = audio_file.read()
    os.remove("current_sentence.mp3")
    return audio_bytes

# 퀴즈 시작 시 초기화
def start_quiz():
    st.session_state.quiz_started = True
    st.session_state.current_index = 0
    st.session_state.score = 0
    prepare_new_question()

# 다음 문제용 셋업
def prepare_new_question():
    current = st.session_state.current_index
    important_words = [sentences[current][i] for i in important_indices[current]]
    st.session_state.shuffled_words = important_words.copy()
    random.shuffle(st.session_state.shuffled_words)
    st.session_state.used_words = []
    st.session_state.selected_words = []

# 단어 선택
def select_word(word):
    if word not in st.session_state.selected_words:
        st.session_state.selected_words.append(word)
        st.session_state.used_words.append(word)

# 정답 확인
def submit_answer():
    correct = [sentences[st.session_state.current_index][i] for i in important_indices[st.session_state.current_index]]
    if st.session_state.selected_words == correct:
        st.session_state.score += 1
        st.success("✅ Correct!")
    else:
        st.error("❌ Incorrect. Try again.")

# 선택 초기화
def clear_selection():
    st.session_state.selected_words = []
    st.session_state.used_words = []

# 다음 문제로 이동
def next_problem():
    if st.session_state.current_index < len(sentences) - 1:
        st.session_state.current_index += 1
        prepare_new_question()
    else:
        st.success(f"🎉 Quiz Complete! Final Score: {st.session_state.score} / {len(sentences)}")
        st.balloons()
        st.session_state.quiz_started = False

# UI 시작
st.title("🧠 Sentence Structure Quiz")

if not st.session_state.quiz_started:
    st.write("Click below to start the quiz! You'll hear a sentence and pick the key words in the correct order.")
    st.button("Start Quiz", on_click=start_quiz)
else:
    st.subheader(f"Question {st.session_state.current_index + 1} of {len(sentences)}")
    audio_bytes = play_tts()
    st.audio(audio_bytes, format="audio/mp3")

    # 문맥 표시
    current_sentence = sentences[st.session_state.current_index]
    important_pos = important_indices[st.session_state.current_index]
    display = []

    for i, word in enumerate(current_sentence):
        if i in important_pos:
            idx = important_pos.index(i)
            filled = st.session_state.selected_words[idx] if idx < len(st.session_state.selected_words) else "___"
            display.append(f"**{filled}**")
        else:
            display.append(word)
    st.markdown("**Context:** " + ' '.join(display))

    # 선택 가능한 단어 버튼
    st.markdown("**Select key words in order:**")
    cols = st.columns(5)
    for idx, word in enumerate(st.session_state.shuffled_words):
        if word not in st.session_state.used_words:
            if cols[idx % 5].button(word, key=f"{word}_{idx}"):
                select_word(word)

    st.markdown("**Selected Words:** " + ' '.join(st.session_state.selected_words))
    st.markdown(f"**Current Score: {st.session_state.score} / {len(sentences)}**")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("✅ Submit", on_click=submit_answer)
    with col2:
        st.button("🔄 Clear", on_click=clear_selection)
    with col3:
        st.button("⏭️ Next", on_click=next_problem)
