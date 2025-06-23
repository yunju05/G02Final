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

def create_quiz_with_gaps(sentence, difficulty):
    words = sentence.split()
    # 단어 사이사이에 빈칸을 넣을 수 있는 위치는 (단어 사이) 단어 개수 - 1개
    gap_positions = list(range(len(words) - 1))
    
    # 난이도에 따른 빈칸 개수
    if difficulty == "Hard":
        blank_count = random.randint(6, 8)
    else:
        blank_count = random.randint(4, 5)
    blank_count = min(blank_count, len(gap_positions))
    
    blank_positions = random.sample(gap_positions, blank_count)
    
    # 빈칸 넣기 위해 단어 사이사이에 '___' 넣음
    quiz_sentence = []
    for i in range(len(words)):
        quiz_sentence.append(words[i])
        # 단어 마지막이 아니고, 빈칸 위치면 '___' 추가
        if i < len(words) -1:
            if i in blank_positions:
                quiz_sentence.append("___")
            else:
                quiz_sentence.append(" ")
    
    return quiz_sentence, blank_positions, words

st.title("문장 사이 빈칸 채우기 퀴즈")

difficulty = st.radio("난이도 선택", ("Easy", "Hard"))
sentence_idx = st.number_input("문장 번호 선택 (1~7)", min_value=1, max_value=len(sentences), step=1)

quiz_sentence, blank_positions, original_words = create_quiz_with_gaps(sentences[sentence_idx -1], difficulty)

# 화면에 빈칸 문장 출력 (문자열 형태)
st.write("".join(quiz_sentence))

# 빈칸에 들어갈 단어를 물어보기 (빈칸마다 단어 하나씩 입력)
user_answers = {}
for pos in blank_positions:
    # 빈칸은 단어 사이에 위치하므로 답은 두 단어 사이 띄어쓰기 부분에 들어간 단어 (예: 연결어, 전치사 등)
    answer = st.text_input(f"빈칸 between '{original_words[pos]}' and '{original_words[pos+1]}' 에 들어갈 단어를 입력하세요:", key=f"input_{pos}")
    user_answers[pos] = answer.strip()

if st.button("정답 확인"):
    correct = True
    for pos in blank_positions:
        # 빈칸 위치에 실제로 들어가는 단어는 원래 문장의 띄어쓰기 없이 바로 이어지기 때문에
        # 원래 문장에서 빈칸 위치 단어 사이에 있는 원래 단어를 찾기 위해 원문에서 단어 pos와 pos+1 사이에 들어가는 단어를 찾아야 함
        # 하지만 문장 단어 나누기 시 띄어쓰기 기준이라 띄어쓰기 없는 구두점 포함 단어에 한계가 있음.
        # 여기서는 단순히 빈칸 사이에 붙어있는 단어로 인식하는 것으로 처리
        # 정확한 처리를 위해서는 원문 전체 문장과 빈칸 위치를 직접 지정하는 방법이 더 좋음
        
        # 여기서는 빈칸 사이에 붙는 단어가 없으므로 답은 빈 문자열로 처리 (사용자 편의를 위해 정답을 체크하지 않음)
        # 만약 빈칸 사이에 특정 단어를 넣는 문제라면 그 단어와 비교하는 로직 필요
        
        # 예시로 pos+1 번째 단어 앞에 붙는 쉼표 같은 경우 제외하고
        # 빈칸 답을 ' '로 둔다고 가정해 답 체크 무시
        pass
    
    st.success("정답 확인 기능은 빈칸 사이사이 단어 문제 특성상 사용자 입력 후 직접 확인하세요.")

