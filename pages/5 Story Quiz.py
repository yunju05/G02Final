import streamlit as st
import random
from gtts import gTTS
import os

# 문장 리스트
sentences = [
    ["Leo", "and", "his", "friends", "discovered", "a", "path", "leading", "to", "the", "Whispering", "Woods", ",", "known", "for", "the", "trees", "that", "could", "talk"],
    ["The", "locals", "avoided", "it,", "saying", "it", "was", "bewitched", ",", "but", "the", "adventurous", "teens", "couldn’t", "resist", "exploring"],
    ["As", "they", "walked", "deeper", "into", "the", "woods", ",", "the", "trees", "started", "whispering"],
    ["Each", "tree", "told", "stories", "of", "ancient", "times", ",", "of", "battles", "fought", "and", "lovers", "separated"],
    ["The", "trees", "also", "warned", "them", "about", "the", "dangers", "of", "forgetting", "the", "past", "and", "the", "importance", "of", "nature"],
    ["Moved", "by", "these", "stories,", "the", "friends", "promised", "to", "protect", "the", "woods", "and", "share", "their", "knowledge"],
    ["They", "left", "the", "woods", "wiser,", "with", "a", "deeper", "respect", "for", "nature", "and", "its", "untold", "stories", ",", "ready", "to", "advocate", "for", "its", "preservation"]
]

# 각 문장에 해당하는 중요한 단어 인덱스 (예: 수동태, 동명사 등)
important_indices = [
    [4, 10, 18],   # "discovered", "Whispering", "talk"
    [2, 6, 15],    # "avoided", "was", "exploring"
    [2, 10],       # "walked", "whispering"
    [2, 9, 13],    # "told", "battles", "separated"
    [3, 9, 14],    # "warned", "forgetting", "importance"
    [6, 8, 12],    # "promised", "protect", "share"
    [4, 7, 17]     # "wiser,", "respect", "advocate"
]

# 초기 상태 설정
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'selected_words' not in st.session_state:
    st.session_state.selected_words = []
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'shuffled_words' not in st.session_state:
    st.session_state.shuffled_words = []

def start_quiz():
    st.session_state.quiz_started = True
    st.session_state.current_index = 0
    st.session_state.selected_words = []
    update_shuffled_words()

def update_shuffled_words():
    important_words = [sentences[st.session_state.current_index][i] for i in important_indices[st.session_state.current_index]]
    st.session_state.shuffled_words = important_words.copy()
    random.shuffle(st.session_state.shuffled_words)

def play_tts():
    current_sentence = ' '.join(sentences[st.session_state.current_index])
    tts = gTTS(current_sentence)
    tts.save("current_sentence.mp3")
    with open("current_sentence.mp3", "rb") as audio_file:
        audio_bytes = audio_file.read()
    os.remove("current_sentence.mp3")
    return audio_bytes

def select_word(word):
    if word not in st.session_state.selected_words:
        st.session_state.selected_words.append(word)

def clear_selection():
    st.session_state.selected_words = []

def submit_answer():
    correct = [sentences[st.session_state.current_index][i] for i in important_indices[st.session_state.current_index]]
    if st.session_state.selected_words == correct:
        st.success("✅ Correct!")
    else:
        st.error("❌ Incorrect. Try again.")

def next_problem():
    if st.session_state.current_index < len(sentences) - 1:
        st.session_state.current_index += 1
        st.session_state.selected_words = []
        update_shuffled_words()
    else:
        st.success("🎉 You've completed all the sentences!")
        st.balloons()
        st.session_state.quiz_started = False

# 인터페이스 시작
st.title("🔡 Sentence Structure Quiz")

if not st.session_state.quiz_started:
    st.write("Start Quiz to review the plot and grammar! You can Click the words in correct order to fill the blank.")
    st.button("Start Quiz", on_click=start_quiz)
else:
    st.subheader(f"Question {st.session_state.current_index + 1}")
    audio_bytes = play_tts()
    st.audio(audio_bytes, format="audio/mp3")

    current_sentence = sentences[st.session_state.current_index]
    important_pos = important_indices[st.session_state.current_index]

    # 문맥 문장 표시 (중요 단어는 빈칸으로)
    display = []
    for i, word in enumerate(current_sentence):
        if i in important_pos:
            idx = important_pos.index(i)
            filled = st.session_state.selected_words[idx] if idx < len(st.session_state.selected_words) else "___"
            display.append(f"**{filled}**")
        else:
            display.append(word)
    st.markdown("**Context:** " + ' '.join(display))

    # 버튼으로 단어 선택
    num_cols = 5
    cols = st.columns(num_cols)
    for idx, word in enumerate(st.session_state.shuffled_words):
        col = cols[idx % num_cols]
        if col.button(word, key=f"{word}_{idx}"):
            select_word(word)

    st.markdown("**Selected:** " + ' '.join(st.session_state.selected_words))

    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("✅ Submit", on_click=submit_answer)
    with col2:
        st.button("🔄 Clear", on_click=clear_selection)
    with col3:
        st.button("⏭️ Next", on_click=next_problem)
