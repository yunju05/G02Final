import streamlit as st
import random
from gtts import gTTS
import os
import pandas as pd

# 문장 리스트
sentences = [
    ["Leo", "and", "his", "friends", "discovered", "a", "path", "leading", "to", "the", "Whispering", "Woods", ",", "known", "for", "the", "trees", "that", "could", "talk"],
    ["The", "locals", "avoided", "it,", "saying", "it", "was", "bewitched", ",", "but", "the", "adventurous", "teens", "couldn’t", "resist", "exploring"],
    ["As", "they", "walked", "deeper", "into", "the", "woods", ",", "the", "trees", "started", "whispering"],
    ["Each", "tree", "told", "stories", "of", "ancient", "times", ",", "of", "battles", "fought", "and", "lovers", "separated"],
    ["The", "trees", "also", "warned", "them", "about", "the", "dangers", "of", "forgetting", "the", "past", "and", "the", "importance", "of", "nature"],
    ["Moved", "by", "these", "stories", ",", "the", "friends", "promised", "to", "protect", "the", "woods", "and", "share", "their", "knowledge"],
    ["They", "left", "the", "woods", "wiser", "," "with", "a", "deeper", "respect", "for", "nature", "and", "its", "untold", "stories", ",", "ready", "to", "advocate", "for", "its", "preservation"]
]

# 중요 단어 인덱스
important_indices = [
    [6, 7, 10, 11, 17, 18, 19],
    [2, 6, 7, 13, 14, 15],
    [2, 3, 10, 11],
    [2, 3, 9, 10, 12, 13],
    [2, 3, 4, 7, 8, 9],
    [1, 2, 3, 4, 8, 9, 10, 14],
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
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'feedback_shown' not in st.session_state:
    st.session_state.feedback_shown = False
if 'result_data' not in st.session_state:
    st.session_state.result_data = []

# 시작 함수
def start_quiz():
    st.session_state.quiz_started = True
    st.session_state.current_index = 0
    st.session_state.selected_words = []
    st.session_state.score = 0
    st.session_state.result_data = []
    st.session_state.feedback_shown = False
    update_shuffled_words()

# 셔플된 중요 단어 준비
def update_shuffled_words():
    important_words = [sentences[st.session_state.current_index][i] for i in important_indices[st.session_state.current_index]]
    st.session_state.shuffled_words = important_words.copy()
    random.shuffle(st.session_state.shuffled_words)

# 음성 출력
def play_tts():
    current_sentence = ' '.join(sentences[st.session_state.current_index])
    tts = gTTS(current_sentence)
    tts.save("tts.mp3")
    with open("tts.mp3", "rb") as f:
        audio_bytes = f.read()
    os.remove("tts.mp3")
    return audio_bytes

# 단어 선택
def select_word(word):
    if word not in st.session_state.selected_words:
        st.session_state.selected_words.append(word)
        if word in st.session_state.shuffled_words:
            st.session_state.shuffled_words.remove(word)

# 초기화
def clear_selection():
    st.session_state.selected_words = []

# 정답 제출
def submit_answer():
    if st.session_state.feedback_shown:
        return
    correct = [sentences[st.session_state.current_index][i] for i in important_indices[st.session_state.current_index]]
    user = st.session_state.selected_words
    is_correct = user == correct

    if is_correct:
        st.success("✅ Correct!")
        st.session_state.score += 1
        st.session_state.feedback_shown = True
        st.session_state.result_data.append({
            "Question": st.session_state.current_index + 1,
            "Correct": True,
            "Your Answer": ' '.join(user),
            "Answer": ' '.join(correct)
        })
    else:
        st.warning("❌ Incorrect. Try again.")

# 정답 보기
def show_answer():
    correct = [sentences[st.session_state.current_index][i] for i in important_indices[st.session_state.current_index]]
    st.info("✅ Correct Answer: " + ' '.join(correct))
    st.session_state.result_data.append({
        "Question": st.session_state.current_index + 1,
        "Correct": False,
        "Your Answer": ' '.join(st.session_state.selected_words),
        "Answer": ' '.join(correct)
    })
    st.session_state.feedback_shown = True

# 다음 문제
def next_problem():
    if st.session_state.current_index < len(sentences) - 1:
        st.session_state.current_index += 1
        st.session_state.selected_words = []
        st.session_state.feedback_shown = False
        update_shuffled_words()
    else:
        st.session_state.quiz_started = False
        st.success(f"🎉 Quiz completed! Final Score: {st.session_state.score} / {len(sentences)}")
        st.balloons()

# 인터페이스 시작
st.title("📚 Sentence Structure Quiz")

if not st.session_state.quiz_started:
    st.write("Click to begin your sentence ordering challenge!")
    if st.button("Start Quiz"):
        start_quiz()
else:
    st.subheader(f"Question {st.session_state.current_index + 1}")
    audio_bytes = play_tts()
    st.audio(audio_bytes, format="audio/mp3")

    current_sentence = sentences[st.session_state.current_index]
    important_pos = important_indices[st.session_state.current_index]

    # 문장 출력
    display = []
    for i, word in enumerate(current_sentence):
        if i in important_pos:
            idx = important_pos.index(i)
            filled = st.session_state.selected_words[idx] if idx < len(st.session_state.selected_words) else "___"
            display.append(f"**{filled}**")
        else:
            display.append(word)
    st.markdown("**Context:** " + ' '.join(display))

    # 단어 버튼
    cols = st.columns(5)
    for idx, word in enumerate(st.session_state.shuffled_words):
        if word:
            col = cols[idx % 5]
            if col.button(word, key=f"{word}_{idx}"):
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

# 결과 저장
if not st.session_state.quiz_started and st.session_state.result_data:
    df = pd.DataFrame(st.session_state.result_data)
    st.subheader("📊 Result Summary")
    st.dataframe(df)
    csv = df.to_csv(index=False).encode('utf-8-sig')
    st.download_button("📥 Download Result (CSV)", data=csv, file_name="quiz_result.csv", mime="text/csv")
