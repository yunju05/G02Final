import streamlit as st
import random

sentences = [
    "Leo and his friends discovered a path leading to the Whispering Woods, known for the trees that could talk.",
    "The locals avoided it, saying it was bewitched, but the adventurous teens couldn’t resist exploring.",
    "As they walked deeper into the woods, the trees started whispering.",
    "Each tree told stories of ancient times, of battles fought and lovers separated.",
    "The trees also warned them about the dangers of forgetting the past and the importance of nature.",
    "Moved by these stories, the friends promised to protect the woods and share their knowledge.",
    "They left the woods wiser, with a deeper respect for nature and its untold stories, ready to advocate for its preservation."
]

def create_inline_input_quiz(sentence, difficulty):
    words = sentence.split()
    indices = [i for i, w in enumerate(words) if w.isalpha() or w.replace(",", "").replace(".", "").isalpha()]
    
    # 난이도에 따라 빈칸 개수 결정
    if difficulty == "Hard":
        blank_count = random.randint(6, 8)
    else:
        blank_count = random.randint(4, 5)
    
    blank_indices = random.sample(indices, min(blank_count, len(indices)))
    return words, blank_indices

st.title("문장 빈칸 채우기 퀴즈 (직접 입력)")

difficulty = st.radio("난이도 선택", ("Easy", "Hard"))
sentence_idx = st.number_input("문장 번호 선택 (1~7)", min_value=1, max_value=len(sentences), step=1)

words, blank_indices = create_inline_input_quiz(sentences[sentence_idx - 1], difficulty)

# 사용자 입력을 저장할 딕셔너리
user_answers = {}

# 문장을 구성하면서 빈칸에 input field 삽입
st.markdown("### 아래 문장의 빈칸을 채워보세요:")

# Streamlit에서 한 줄에 문장 + input 박스를 표현하기 위해 container 사용
quiz_row = st.container()
with quiz_row:
    quiz_col = st.columns(len(words))
    for i, word in enumerate(words):
        if i in blank_indices:
            user_input = quiz_col[i].text_input(label="", placeholder="?", key=f"blank_{i}")
            user_answers[i] = user_input.strip()
        else:
            quiz_col[i].markdown(f"**{word}**")

# 정답 확인
if st.button("정답 확인"):
    original_words = sentences[sentence_idx - 1].split()
    correct = True
    for idx in blank_indices:
        if user_answers.get(idx, "").lower() != original_words[idx].strip(".,").lower():
            correct = False
            st.write(f"❌ 빈칸 {idx+1}: 입력한 단어 **{user_answers[idx]}**, 정답은 **{original_words[idx]}**")
    if correct:
        st.success("모든 답이 맞았습니다! 🎉")
    else:
        st.warning("일부 답이 틀렸습니다. 위의 피드백을 확인하세요.")
