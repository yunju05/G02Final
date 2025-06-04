import streamlit as st
import random
from gtts import gTTS
import os
import pandas as pd

# 문장 리스트 및 인덱스
sentences = [
    ["Leo", "and", "his", "friends", "discovered", "a", "path", "leading", "to", "the", "Whispering", "Woods", ",", "known", "for", "the", "trees", "that", "could", "talk"],
    ["The", "locals", "avoided", "it,", "saying", "it", "was", "bewitched", ",", "but", "the", "adventurous", "teens", "couldn’t", "resist", "exploring"],
    ["As", "they", "walked", "deeper", "into", "the", "woods", ",", "the", "trees", "started", "whispering"],
    ["Each", "tree", "told", "stories", "of", "ancient", "times", ",", "of", "battles", "fought", "and", "lovers", "separated"],
    ["The", "trees", "also", "warned", "them", "about", "the", "dangers", "of", "forgetting", "the", "past", "and", "the", "importance", "of", "nature"],
    ["Moved", "by", "these", "stories", ",", "the", "friends", "promised", "to", "protect", "the", "woods", "and", "share", "their", "knowledge"],
    ["They", "left", "the", "woods", "wiser", ",", "with", "a", "deeper", "respect", "for", "nature", "and", "its", "untold", "stories", ",", "ready", "to", "advocate", "for", "its", "preservation"]
]

# Hard 모드용 핵심 단어 인덱스
important_indices_hard = [
    [6, 7, 10, 11, 17, 18, 19],
    [2, 6, 7, 13, 14, 15],
    [2, 3, 10, 11],
    [2, 3, 9, 10, 12, 13],
    [2, 3, 4, 7, 8, 9],
    [1, 2, 3, 8, 9, 10, 14],
    [4, 8, 9, 13, 14, 15, 17, 18, 22]
]

# Easy 모드용 더 짧은 핵심 단어 인덱스 (주로 동사 위주)
important_indices_easy = [
    [4], [2], [2], [2], [3], [7], [4]
]

# 상태 초기화
defaults = {
    'current_index': 0,
    'selected_words': [],
    'used_words': [],
    'quiz_started': False,
    'shuffled_words': [],
    'score': 0,
    'feedback_shown': False,
    'result_data': [],
    'difficulty': 'Hard'
}
for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

def get_current_indices():
    return important_indices_easy if st.session_state.difficulty == "Easy" else important_indices_hard

# 퀴즈 시작
def start_quiz():
    st.session_state.quiz_started = True
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.result_data = []
    prepare_new_question()

def prepare_new_question():
    important_words = [sentences[st.session_state.current_index][i] for i in get_current_indices()[st.session_state.current_index]]
    st.session_state.shuffled_words = random.sample(important_words, len(important_words))
    st.session_state.selected_words = []
    st.session_state.used_words = []
    st.session_state.feedback_shown = False

def play_tts():
    sentence = ' '.join(sentences[st.session_state.current_index])
    tts = gTTS(sentence)
    tts.save("tts.mp3")
    with open("tts.mp3", "rb") as f:
        audio = f.read()
    os.remove("tts.mp3")
    return audio

def select_word(word):
    if word not in st.session_state.used_words:
        st.session_state.selected_words.append(word)
        st.session_state.used_words.append(word)

def clear_selection():
    st.session_state.selected_words = []
    st.session_state.used_words = []

def submit_answer():
    if st.session_state.feedback_shown:
        return
    correct = [sentences[st.session_state.current_index][i] for i in get_current_indices()[st.session_state.current_index]]
    is_correct = st.session_state.selected_words == correct
    if is_correct:
        st.success("✅ Correct!")
        st.session_state.score += 1
        st.session_state.result_data.append({
            "Question": st.session_state.current_index + 1,
            "Correct": True,
            "Your Answer": ' '.join(st.session_state.selected_words),
            "Answer": ' '.join(correct)
        })
        st.session_state.feedback_shown = True
    else:
        st.warning("❌ Incorrect. Try again.")

def show_answer():
    correct = [sentences[st.session_state.current_index][i] for i in get_current_indices()[st.session_state.current_index]]
    st.info("✅ Answer: " + ' '.join(correct))
    st.session_state.result_data.append({
        "Question": st.session_state.current_index + 1,
        "Correct": False,
        "Your Answer": ' '.join(st.session_state.selected_words),
        "Answer": ' '.join(correct)
    })
    st.session_state.feedback_shown = True

def next_problem():
    if st.session_state.current_index < len(sentences) - 1:
        st.session_state.current_index += 1
        prepare_new_question()
    else:
        st.success(f"🎉 Quiz Complete! Final Score: {st.session_state.score} / {len(sentences)}")
        st.balloons()
        st.session_state.quiz_started = False

# UI
st.title("🧠 Sentence Structure Quiz")

if not st.session_state.quiz_started:
    st.selectbox("🧩 Choose difficulty level:", ["Easy", "Hard"], key='difficulty')
    st.write("Choose the correct words to complete the story sentences based on the difficulty.")
    if st.button("Start Quiz"):
        start_quiz()
else:
    st.subheader(f"Question {st.session_state.current_index + 1} ({st.session_state.difficulty})")
    st.audio(play_tts(), format="audio/mp3")

    current_sentence = sentences[st.session_state.current_index]
    important_pos = get_current_indices()[st.session_state.current_index]

    display = []
    for i, word in enumerate(current_sentence):
        if i in important_pos:
            idx = important_pos.index(i)
            filled = st.session_state.selected_words[idx] if idx < len(st.session_state.selected_words) else "___"
            display.append(f"**{filled}**")
        else:
            display.append(word)
    st.markdown("**Context:** " + ' '.join(display))

    st.markdown("### 🔡 Select the key words:")
    cols = st.columns(5)
    for idx, word in enumerate(st.session_state.shuffled_words):
        if word not in st.session_state.used_words:
            if cols[idx % 5].button(word, key=f"{word}_{idx}"):
                select_word(word)

    st.markdown("**Selected:** " + ' '.join(st.session_state.selected_words))
    st.markdown(f"**Score:** {st.session_state.score} / {len(sentences)}")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.button("✅ Submit", on_click=submit_answer)
    with col2:
        st.button("🔄 Clear", on_click=clear_selection)
    with col3:
        st.button("👀 Show Answer", on_click=show_answer, disabled=st.session_state.feedback_shown)
    with col4:
        st.button("⏭️ Next", on_click=next_problem, disabled=not st.session_state.feedback_shown)

if not st.session_state.quiz_started and st.session_state.result_data:
    df = pd.DataFrame(st.session_state.result_data)
    st.subheader("📊 Results Summary")
    st.dataframe(df)
    csv = df.to_csv(index=False).encode('utf-8-sig')
    st.download_button("Download CSV", data=csv, file_name="quiz_results.csv", mime="text/csv")
