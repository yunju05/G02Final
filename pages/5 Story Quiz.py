import streamlit as st
import random

# 1. 문장 리스트 (연결된 문장 형태)
sentences = [
    "Leo and his friends discovered a path leading to the Whispering Woods, known for the trees that could talk.",
    "The locals avoided it, saying it was bewitched, but the adventurous teens couldn’t resist exploring.",
    "As they walked deeper into the woods, the trees started whispering.",
    "Each tree told stories of ancient times, of battles fought and lovers separated.",
    "The trees also warned them about the dangers of forgetting the past and the importance of nature.",
    "Moved by these stories, the friends promised to protect the woods and share their knowledge.",
    "They left the woods wiser, with a deeper respect for nature and its untold stories, ready to advocate for its preservation."
]

def create_quiz(sentence, difficulty):
    words = sentence.split()
    length = len(words)

    # 빈칸 개수 난이도별로 결정
    if difficulty == "Hard":
        blank_count = random.randint(6, 8)
    else:  # Easy
        blank_count = random.randint(4, 5)
    
    # 빈칸으로 만들 단어 인덱스 랜덤 추출 (단, 쉼표 등 문장 부호 제외)
    candidate_indices = [i for i, w in enumerate(words) if w.isalpha()]
    blank_indices = random.sample(candidate_indices, min(blank_count, len(candidate_indices)))

    quiz_words = []
    for i, w in enumerate(words):
        if i in blank_indices:
            quiz_words.append("___")
        else:
            quiz_words.append(w)
    
    return quiz_words, blank_indices, words

st.title("문장 빈칸 채우기 퀴즈")

difficulty = st.radio("난이도 선택", ("Easy", "Hard"))

sentence_idx = st.number_input("문장 번호 선택 (1~7)", min_value=1, max_value=len(sentences), step=1)

quiz_words, blank_indices, original_words = create_quiz(sentences[sentence_idx - 1], difficulty)

st.write("문장:")
st.write(" ".join(quiz_words))

user_answers = {}
for idx in blank_indices:
    user_input = st.text_input(f"빈칸 단어 {idx+1} 입력:", key=f"input_{idx}")
    user_answers[idx] = user_input.strip()

if st.button("정답 확인"):
    correct = True
    for idx in blank_indices:
        if user_answers.get(idx, "").lower() != original_words[idx].lower():
            correct = False
            break
    if correct:
        st.success("모든 답이 맞았습니다! 🎉")
    else:
        st.error("틀린 답이 있습니다. 다시 시도해보세요.")
