import streamlit as st
import random

# ✅ 문장 데이터
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
def init_session_state():
    if "blank_indices" not in st.session_state:
        st.session_state.blank_indices = []
    if "blank_answers" not in st.session_state:
        st.session_state.blank_answers = {}
    if "available_words" not in st.session_state:
        st.session_state.available_words = []
    if "original_words" not in st.session_state:
        st.session_state.original_words = []
    if "current_sentence_index" not in st.session_state:
        st.session_state.current_sentence_index = 0
    if "trigger_rerun" not in st.session_state:
        st.session_state.trigger_rerun = False

init_session_state()

# ✅ 퀴즈 초기화 함수
def initialize_quiz(sentence_idx, difficulty):
    sentence = sentences[sentence_idx]
    words = sentence.split()
    st.session_state.original_words = words

    candidate_indices = [i for i, w in enumerate(words) if w.isalpha() or w.replace(",", "").replace(".", "").isalpha()]

    num_blanks = random.randint(6, 8) if difficulty == "Hard" else random.randint(4, 5)
    blank_indices = sorted(random.sample(candidate_indices, min(num_blanks, len(candidate_indices))))
    st.session_state.blank_indices = blank_indices
    st.session_state.blank_answers = {idx: "" for idx in blank_indices}
    st.session_state.available_words = [words[idx].strip(".,") for idx in blank_indices]
    random.shuffle(st.session_state.available_words)

# ✅ UI
st.title("📘 문장 빈칸 채우기 퀴즈")

difficulty = st.radio("난이도 선택", ("Easy", "Hard"))
sentence_idx = st.number_input("문장 번호 선택 (1~7)", min_value=1, max_value=7, step=1) - 1

if st.button("퀴즈 시작"):
    st.session_state.current_sentence_index = sentence_idx
    initialize_quiz(sentence_idx, difficulty)
    st.session_state.trigger_rerun = True  # 퀴즈 시작 시에도 rerun

# ✅ 퀴즈 표시
if st.session_state.original_words:
    st.markdown("### 📝 아래 문장의 빈칸을 채우세요:")

    # 문장 출력 (빈칸 포함)
    sentence_display = []
    for i, word in enumerate(st.session_state.original_words):
        if i in st.session_state.blank_indices:
            filled = st.session_state.blank_answers.get(i, "")
            sentence_display.append(f"`{filled if filled else '_____ '}`")
        else:
            sentence_display.append(word)
    st.markdown(" ".join(sentence_display))

    # 단어 버튼 출력
    st.markdown("### 선택할 수 있는 단어들:")
    if st.session_state.available_words:
        cols = st.columns(len(st.session_state.available_words))
        for i, word in enumerate(st.session_state.available_words[:]):  # 복사본 사용
            if cols[i].button(word, key=f"word_btn_{word}"):
                # 첫 번째 빈칸에 넣기
                for idx in st.session_state.blank_indices:
                    if st.session_state.blank_answers[idx] == "":
                        st.session_state.blank_answers[idx] = word
                        break
                st.session_state.available_words.remove(word)
                st.session_state.trigger_rerun = True  # rerun flag만 설정

    # 정답 확인
    if st.button("정답 확인"):
        correct = True
        for idx in st.session_state.blank_indices:
            user_word = st.session_state.blank_answers[idx].lower().strip()
            correct_word = st.session_state.original_words[idx].strip(".,").lower()
            if user_word != correct_word:
                st.error(f"❌ `{user_word}` → 정답은 `{correct_word}`")
                correct = False
        if correct:
            st.success("🎉 정답입니다!")

    # 다시 풀기
    if st.button("🔄 다시 풀기"):
        initialize_quiz(st.session_state.current_sentence_index, difficulty)
        st.session_state.trigger_rerun = True

# ✅ rerun은 UI가 모두 그려진 후에 마지막에 실행
if st.session_state.trigger_rerun:
    st.session_state.trigger_rerun = False  # 무한 루프 방지
    st.experimental_rerun()
