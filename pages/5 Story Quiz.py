import streamlit as st
import random
from gtts import gTTS
import os
import pandas as pd

# 문장 리스트 및 번역
sentences = [
    ["Leo", "and", "his", "friends", "discovered", "a", "path", "leading", "to", "the", "Whispering", "Woods", ",", "known", "for", "the", "trees", "that", "could", "talk"],
    ["The", "locals", "avoided", "it,", "saying", "it", "was", "bewitched", ",", "but", "the", "adventurous", "teens", "couldn’t", "resist", "exploring"],
    ["As", "they", "walked", "deeper", "into", "the", "woods", ",", "the", "trees", "started", "whispering"],
    ["Each", "tree", "told", "stories", "of", "ancient", "times", ",", "of", "battles", "fought", "and", "lovers", "separated"],
    ["The", "trees", "also", "warned", "them", "about", "the", "dangers", "of", "forgetting", "the", "past", "and", "the", "importance", "of", "nature"],
    ["Moved", "by", "these", "stories", ",", "the", "friends", "promised", "to", "protect", "the", "woods", "and", "share", "their", "knowledge"],
    ["They", "left", "the", "woods", "wiser", ",", "with", "a", "deeper", "respect", "for", "nature", "and", "its", "untold", "stories", ",", "ready", "to", "advocate", "for", "its", "preservation"]
]

translations = [
    "리오와 그의 친구들은 속삭이는 숲으로 이어지는 길을 발견했다.",
    "현지인들은 그 숲이 마법에 걸렸다고 해서 피했지만, 모험심 강한 십대들은 탐험을 멈추지 않았다.",
    "그들이 숲 속으로 더 깊이 들어가자, 나무들이 속삭이기 시작했다.",
    "각 나무는 오래전의 전쟁과 이별 이야기를 들려주었다.",
    "나무들은 과거를 잊지 말고 자연을 소중히 하라고 경고했다.",
    "그 이야기에 감동한 친구들은 숲을 보호하고 이야기를 전하기로 약속했다.",
    "그들은 자연과 그것의 숨겨진 이야기들에 대한 깊은 존경심을 가지고 숲을 떠났다."
]

important_indices_hard = [
    [6, 7, 10, 11, 17, 18, 19],
    [2, 6, 7, 13, 14, 15],
    [2, 3, 10, 11],
    [2, 3, 9, 10, 12, 13],
    [2, 3, 4, 7, 8, 9],
    [1, 2, 3, 8, 9, 10, 14],
    [4, 8, 9, 13, 14, 15, 17, 18, 22]
]

important_indices_easy = [
    [4], [2], [2], [2], [3], [7], [4]
]

# 🔧 상태 초기화
defaults = {
    'current_index': 0,
    'selected_words': [],
    'used_words': [],
    'quiz_started': False,
    'shuffled_words': [],
    'score': 0,
    'feedback_shown': False,
    'result_data': [],
    'difficulty': 'Hard'  # 기본값 설정
}
for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# 추가 안전장치 (예방적 중복 방지)
if 'difficulty' not in st.session_state:
    st.session_state.difficulty = 'Hard'

def get_current_indices():
    return important_indices_easy if st.session_state.difficulty == "Easy" else important_indices_hard

def start_quiz():
    st.session_state.quiz_started = True
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.result_data = []
    prepare_new_question()

def prepare_new_question():
    sentence = sentences[st.session_state.current_index]
    if st.session_state.difficulty == "Easy":
        indices = get_current_indices()[st.session_state.current_index]
        selected = [sentence[i] for i in indices]
    else:
        selected = sentence
    st.session_state.shuffled_words = random.sample(selected, len(selected))
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
    sentence = sentences[st.session_state.current_index]
    if st.session_state.difficulty == "Easy":
        correct = [sentence[i] for i in get_current_indices()[st.session_state.current_index]]
    else:
        correct = sentence
    is_correct = st.session_state.selected_words == correct
    if is_correct:
        st.success("✅ Correct sentence structure!")
        st.session_state.score += 1
    else:
        st.warning("❌ Incorrect sentence structure.")
    st.session_state.result_data.append({
        "Question": st.session_state.current_index + 1,
        "Correct": is_correct,
        "Your Answer": ' '.join(st.session_state.selected_words),
        "Answer": ' '.join(correct)
    })
    st.session_state.feedback_shown = True

def show_answer():
    if 'difficulty' not in st.session_state:
        st.warning("⚠️ Please start the quiz first.")
        return
    sentence = sentences[st.session_state.current_index]
    if st.session_state.difficulty == "Easy":
        correct = [sentence[i] for i in get_current_indices()[st.session_state.current_index]]
    else:
        correct = sentence
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

# 📋 UI 시작
st.title("🧠 Sentence Structure Quiz")

if not st.session_state.quiz_started:
    st.selectbox("🧩 Choose difficulty level:", ["Easy", "Hard"], key='difficulty')
    st.write("Choose the correct words to complete the story sentences based on the difficulty.")
    if st.button("Start Quiz"):
        start_quiz()
else:
    st.subheader(f"Question {st.session_state.current_index + 1} ({st.session_state.difficulty})")

    if st.session_state.difficulty == "Hard":
        st.markdown("### 📘 Korean Translation")
        st.info(translations[st.session_state.current_index])

    st.markdown("### ✍️ Arrange the words to form the correct sentence:")
    st.markdown("**Your Sentence:** " + ' '.join(st.session_state.selected_words))

    st.markdown("### 🔡 Select the key words:")
    cols = st.columns(6)
    for idx, word in enumerate(st.session_state.shuffled_words):
        if word not in st.session_state.used_words:
            if cols[idx % 6].button(word, key=f"{word}_{idx}"):
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

    with st.expander("🔊 Need to hear the sentence? (Click to expand)"):
        if st.button("▶️ Play Sentence Audio"):
            st.audio(play_tts(), format="audio/mp3")

if not st.session_state.quiz_started and st.session_state.result_data:
    df = pd.DataFrame(st.session_state.result_data)
    st.subheader("📊 Results Summary")
    st.dataframe(df)
    csv = df.to_csv(index=False).encode('utf-8-sig')
    st.download_button("Download CSV", data=csv, file_name="quiz_results.csv", mime="text/csv")
