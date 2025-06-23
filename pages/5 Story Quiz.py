import streamlit as st
import random
from gtts import gTTS
import os
import pandas as pd

# 데이터
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

important_indices = {
    "Easy": [
        [4], [2], [2], [2], [3], [7], [4]
    ],
    "Hard": [
        [6, 7, 10, 11, 17, 18, 19],
        [2, 6, 7, 13, 14, 15],
        [2, 3, 10, 11],
        [2, 3, 9, 10, 12, 13],
        [2, 3, 4, 7, 8, 9],
        [1, 2, 3, 8, 9, 10, 14],
        [4, 8, 9, 13, 14, 15, 17, 18, 22]
    ]
}

# 공통 함수 정의
def get_key(mode, name):
    return f"{mode.lower()}_{name}"

def init_state(mode):
    for key, value in {
        'current_index': 0,
        'selected_words': [],
        'used_words': [],
        'quiz_started': False,
        'shuffled_words': [],
        'score': 0,
        'feedback_shown': False,
        'result_data': []
    }.items():
        session_key = get_key(mode, key)
        if session_key not in st.session_state:
            st.session_state[session_key] = value

def prepare_new_question(mode):
    idx = st.session_state[get_key(mode, 'current_index')]
    sentence = sentences[idx]
    indices = important_indices[mode][idx]
    selected = sentence if mode == "Hard" else [sentence[i] for i in indices]
    st.session_state[get_key(mode, 'shuffled_words')] = random.sample(selected, len(selected))
    st.session_state[get_key(mode, 'selected_words')] = []
    st.session_state[get_key(mode, 'used_words')] = []
    st.session_state[get_key(mode, 'feedback_shown')] = False

def play_tts(sentence):
    tts = gTTS(' '.join(sentence))
    tts.save("tts.mp3")
    audio = open("tts.mp3", "rb").read()
    os.remove("tts.mp3")
    return audio

def submit_answer(mode):
    if st.session_state[get_key(mode, 'feedback_shown')]:
        return
    idx = st.session_state[get_key(mode, 'current_index')]
    sentence = sentences[idx]
    correct = sentence if mode == "Hard" else [sentence[i] for i in important_indices[mode][idx]]
    selected = st.session_state[get_key(mode, 'selected_words')]
    is_correct = selected == correct
    if is_correct:
        st.success("✅ Correct!")
        st.session_state[get_key(mode, 'score')] += 1
    else:
        st.warning("❌ Incorrect.")
    st.session_state[get_key(mode, 'result_data')].append({
        "Question": idx + 1,
        "Correct": is_correct,
        "Your Answer": ' '.join(selected),
        "Answer": ' '.join(correct)
    })
    st.session_state[get_key(mode, 'feedback_shown')] = True

def next_problem(mode):
    if st.session_state[get_key(mode, 'current_index')] < len(sentences) - 1:
        st.session_state[get_key(mode, 'current_index')] += 1
        prepare_new_question(mode)
    else:
        st.success(f"🎉 Quiz Complete! Final Score: {st.session_state[get_key(mode, 'score')]} / {len(sentences)}")
        st.balloons()
        st.session_state[get_key(mode, 'quiz_started')] = False

# 탭 UI
st.title("🧠 Sentence Structure Quiz")
tabs = st.tabs(["🟢 Easy Mode", "🔴 Hard Mode"])

for i, mode in enumerate(["Easy", "Hard"]):
    with tabs[i]:
        init_state(mode)
        quiz_started = st.session_state[get_key(mode, 'quiz_started')]

        if not quiz_started:
            if st.button(f"Start {mode} Quiz", key=f"start_{mode}"):
                st.session_state[get_key(mode, 'quiz_started')] = True
                st.session_state[get_key(mode, 'current_index')] = 0
                st.session_state[get_key(mode, 'score')] = 0
                st.session_state[get_key(mode, 'result_data')] = []
                prepare_new_question(mode)
        else:
            idx = st.session_state[get_key(mode, 'current_index')]
            sentence = sentences[idx]

            st.subheader(f"Question {idx + 1} ({mode})")

            if mode == "Hard":
                st.markdown("### 📘 Korean Translation")
                st.info(translations[idx])

            st.markdown("### ✍️ Arrange the words to form the correct sentence:")
            st.markdown("**Your Sentence:** " + ' '.join(st.session_state[get_key(mode, 'selected_words')]))

            st.markdown("### 🔡 Select the key words:")
            cols = st.columns(6)
            for j, word in enumerate(st.session_state[get_key(mode, 'shuffled_words')]):
                if word not in st.session_state[get_key(mode, 'used_words')]:
                    if cols[j % 6].button(word, key=f"{mode}_{word}_{j}"):
                        st.session_state[get_key(mode, 'selected_words')].append(word)
                        st.session_state[get_key(mode, 'used_words')].append(word)

            st.markdown(f"**Score:** {st.session_state[get_key(mode, 'score')]} / {len(sentences)}")

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.button("✅ Submit", on_click=submit_answer, args=(mode,))
            with col2:
                if st.button("🔄 Clear"):
                    st.session_state[get_key(mode, 'selected_words')] = []
                    st.session_state[get_key(mode, 'used_words')] = []
            with col3:
                if st.button("👀 Show Answer", disabled=st.session_state[get_key(mode, 'feedback_shown')]):
                    correct = sentence if mode == "Hard" else [sentence[i] for i in important_indices[mode][idx]]
                    st.info("✅ Answer: " + ' '.join(correct))
                    st.session_state[get_key(mode, 'feedback_shown')] = True
            with col4:
                st.button("⏭️ Next", on_click=next_problem, args=(mode,), disabled=not st.session_state[get_key(mode, 'feedback_shown')])

            with st.expander("🔊 Need to hear the sentence?"):
                if st.button("▶️ Play Sentence Audio", key=f"{mode}_tts"):
                    st.audio(play_tts(sentence), format="audio/mp3")

        # 결과 요약
        if not st.session_state[get_key(mode, 'quiz_started')] and st.session_state[get_key(mode, 'result_data')]:
            st.subheader("📊 Results Summary")
            df = pd.DataFrame(st.session_state[get_key(mode, 'result_data')])
            st.dataframe(df)
            csv = df.to_csv(index=False).encode('utf-8-sig')
            st.download_button("Download CSV", data=csv, file_name=f"{mode.lower()}_quiz_results.csv", mime="text/csv")
