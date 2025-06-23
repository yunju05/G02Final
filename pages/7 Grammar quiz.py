import streamlit as st
import random

# UI 제목
st.title("🔠 Passive Voice Word Order Quiz")

# 📘 Instructions
st.title("🔠 Passive Voice Word Order Quiz")

st.markdown("""
### 📘 How to Play

Practice forming passive voice sentences by arranging the shuffled words.

**Instructions:**
1. Read the **active sentence** at the top.  
   Example: `Tom eats an apple.`

2. Click the words **in the correct order** to form the passive voice.  
   Example: `An apple is eaten by Tom`

3. Selected words will appear under **📝 Your Sentence**.

4. Use the buttons below:
   - ✅ **Submit**: Check your answer.
   - 🔄 **Clear**: Reset your selection.
   - ⏭️ **Next**: Move to the next sentence *(only after a correct answer)*.

**Note:**  
- Each word can be selected **only once**.  
- You must match the **exact word order** to be correct.

---

🎯 *This activity helps you understand passive voice structure and improves your English grammar skills!*
""")

# 문제 은행
quiz_bank = [
    {
        "active": "Tom eats an apple.",
        "passive": ["An", "apple", "is", "eaten", "by", "Tom"]
    },
    {
        "active": "She cleans the room.",
        "passive": ["The", "room", "is", "cleaned", "by", "her"]
    },
    {
        "active": "They watch a movie.",
        "passive": ["A", "movie", "is", "watched", "by", "them"]
    },
    {
        "active": "He reads a book.",
        "passive": ["A", "book", "is", "read", "by", "him"]
    },
    {
        "active": "The dog bites the man.",
        "passive": ["The", "man", "is", "bitten", "by", "the", "dog"]
    }
]

# 상태 초기화
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'selected_words' not in st.session_state:
    st.session_state.selected_words = []
if 'used_words' not in st.session_state:
    st.session_state.used_words = []
if 'shuffled_words' not in st.session_state:
    st.session_state.shuffled_words = []
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'feedback_shown' not in st.session_state:
    st.session_state.feedback_shown = False

# 새 문제 로드
def load_question():
    question = quiz_bank[st.session_state.current_index]
    st.session_state.selected_words = []
    st.session_state.used_words = []
    st.session_state.feedback_shown = False
    st.session_state.shuffled_words = random.sample(question["passive"], len(question["passive"]))

# 단어 선택
def select_word(word):
    if word not in st.session_state.used_words:
        st.session_state.selected_words.append(word)
        st.session_state.used_words.append(word)

# 초기 문제 로딩
if not st.session_state.shuffled_words:
    load_question()

# 현재 문제 가져오기
question = quiz_bank[st.session_state.current_index]
st.markdown(f"### ✅ Active Sentence:\n`{question['active']}`")

st.markdown("### 🔤 Arrange the Passive Sentence:")

# 단어 선택 버튼
cols = st.columns(5)
for idx, word in enumerate(st.session_state.shuffled_words):
    if word not in st.session_state.used_words:
        if cols[idx % 5].button(word, key=f"word_{idx}"):
            select_word(word)

# 선택한 문장 표시
st.markdown("**📝 Your Sentence:**")
st.markdown(" ".join(st.session_state.selected_words) or "`(No words selected yet)`")

# 버튼 영역
col1, col2, col3 = st.columns(3)

# Submit
with col1:
    if st.button("✅ Submit"):
        if st.session_state.selected_words == question["passive"]:
            st.success("🎉 Correct!")
            st.session_state.score += 1
            st.session_state.feedback_shown = True
        else:
            st.error("❌ Incorrect. Try again.")

# Clear
with col2:
    if st.button("🔄 Clear"):
        st.session_state.selected_words = []
        st.session_state.used_words = []
        st.session_state.feedback_shown = False

# Next
with col3:
    if st.button("⏭️ Next"):
        if st.session_state.feedback_shown:
            st.session_state.current_index = (st.session_state.current_index + 1) % len(quiz_bank)
            load_question()
        else:
            st.warning("⚠️ Please submit the correct answer before moving on.")

# 점수 표시
st.markdown(f"### 📊 Score: {st.session_state.score} / {len(quiz_bank)}")
