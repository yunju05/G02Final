import streamlit as st
import random

# ✅ 원본 문장 리스트
sentences = [
    "Leo and his friends discovered a path leading to the Whispering Woods, known for the trees that could talk.",
    "The locals avoided it, saying it was bewitched, but the adventurous teens couldn’t resist exploring.",
    "As they walked deeper into the woods, the trees started whispering.",
    "Each tree told stories of ancient times, of battles fought and lovers separated.",
    "The trees also warned them about the dangers of forgetting the past and the importance of nature.",
    "Moved by these stories, the friends promised to protect the woods and share their knowledge.",
    "They left the woods wiser, with a deeper respect for nature and its untold stories, ready to advocate for its preservation."
]

# ✅ 세션 상태 초기화
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
    st.session_state.blank_indices = []
    st.session_state.blank_answers = {}
    st.session_state.available_words = []
    st.session_state.original_words = []
    st.session_state.current_sentence_index = 0

# ✅ 퀴즈 초기화 함수
def initialize_quiz(sentence_idx, difficulty):
    sentence = sentences[sentence_idx]
    words = sentence.split()
    st.session_state.original_words = words
    st.session_state.current_sentence_index = sentence_idx

    # 단어 위치 인덱스
    candidate_indices = [i for i, w in enumerate(words) if w.isalpha() or w.replace(",", "").replace(".", "").isalpha()]
    num_blanks = random.randint(6, 8) if difficulty == "Hard" else random.randint(4, 5)
    blank_indices = sorted(random.sample(candidate_indices, min(num_blanks, len(candidate_indices))))

    st.session_state.blank_indices = blank_indices
    st.session_state.blank_answers = {i: "" for i in blank_indices}
    st.session_state.available_words = [words[i].strip(".,") for i in blank_indices]
    random.shuffle(st.session_state.available_words)
    st.session_state.quiz_started = True

# ✅ UI 시작
st.title("📘 문장 빈칸 채우기 퀴즈 (안정화 버전)")

difficulty = st.radio("난이도 선택", ("Easy", "Hard"))
sentence_idx = st.number_input("문장 번호 선택 (1~7)", min_value=1, max_value=7, step=1) - 1

if st.button("퀴즈 시작"):
    initialize_quiz(sentence_idx, difficulty)

# ✅ 퀴즈 화면
if st.session_state.quiz_started:
    st.markdown("### 📝 문장의 빈칸을 채워보세요:")

    sentence_display = []
    for i, word in enumerate(st.session_state.original_words):
        if i in st.session_state.blank_indices:
            filled = st.session_state.blank_answers.get(i, "")
            sentence_display.append(f"`{filled if filled else '_____ '}`")
        else:
            sentence_display.append(word)
    st.markdown(" ".join(sentence_display))

    # 단어 버튼
    st.markdown("### 선택할 수 있는 단어들:")
    if st.session_state.available_words:
        cols = st.columns(len(st.session_state.available_words))
        for i, word in enumerate(st.session_state.available_words[:]):  # 복사본 순회
            if cols[i].button(word, key=f"word_btn_{word}"):
                for idx in st.session_state.blank_indices:
                    if st.session_state.blank_answers[idx] == "":
                        st.session_state.blank_answers[idx] = word
                        break
                st.session_state.available_words.remove(word)

    # 정답 확인
    if st.button("정답 확인"):
        correct = True
        for idx in st.session_state.blank_indices:
            user = st.session_state.blank_answers[idx].lower().strip()
            answer = st.session_state.original_words[idx].strip(".,").lower()
            if user != answer:
                st.error(f"❌ `{user}` → 정답은 `{answer}`")
                correct = False
        if correct:
            st.success("🎉 정답입니다! 완벽해요!")

    # 다시 풀기
    if st.button("🔄 다시 풀기"):
        initialize_quiz(st.session_state.current_sentence_index, difficulty)
