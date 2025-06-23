import streamlit as st
import random

# ✅ Original sentence data
sentences = [
    "Leo and his friends discovered a path leading to the Whispering Woods, known for the trees that could talk.",
    "The locals avoided it, saying it was bewitched, but the adventurous teens couldn’t resist exploring.",
    "As they walked deeper into the woods, the trees started whispering.",
    "Each tree told stories of ancient times, of battles fought and lovers separated.",
    "The trees also warned them about the dangers of forgetting the past and the importance of nature.",
    "Moved by these stories, the friends promised to protect the woods and share their knowledge.",
    "They left the woods wiser, with a deeper respect for nature and its untold stories, ready to advocate for its preservation."
]

# ✅ Initialize session state
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
    st.session_state.blank_indices = []
    st.session_state.blank_answers = {}
    st.session_state.available_words = []
    st.session_state.original_words = []
    st.session_state.current_sentence_index = 0

# ✅ Quiz initializer
def initialize_quiz(sentence_idx, difficulty):
    sentence = sentences[sentence_idx]
    words = sentence.split()
    st.session_state.original_words = words
    st.session_state.current_sentence_index = sentence_idx

    candidate_indices = [i for i, w in enumerate(words) if w.isalpha() or w.replace(",", "").replace(".", "").isalpha()]
    num_blanks = random.randint(6, 8) if difficulty == "Hard" else random.randint(4, 5)
    blank_indices = sorted(random.sample(candidate_indices, min(num_blanks, len(candidate_indices))))

    st.session_state.blank_indices = blank_indices
    st.session_state.blank_answers = {i: "" for i in blank_indices}
    st.session_state.available_words = [words[i].strip(".,") for i in blank_indices]
    random.shuffle(st.session_state.available_words)
    st.session_state.quiz_started = True

# ✅ UI
st.title("📘 Sentence Fill-in-the-Blank Quiz")

difficulty = st.radio("Select difficulty", ("Easy", "Hard"))
sentence_idx = st.number_input("Select sentence (1 to 7)", min_value=1, max_value=7, step=1) - 1

if st.button("Start Quiz"):
    initialize_quiz(sentence_idx, difficulty)

# ✅ Quiz display
if st.session_state.quiz_started:
    st.markdown("### 📝 Fill in the blanks in the sentence:")

    # Display sentence with blanks
    sentence_display = []
    for i, word in enumerate(st.session_state.original_words):
        if i in st.session_state.blank_indices:
            filled = st.session_state.blank_answers.get(i, "")
            sentence_display.append(f"`{filled if filled else '_____ '}`")
        else:
            sentence_display.append(word)
    st.markdown(" ".join(sentence_display))

    # Word buttons
    st.markdown("### Select a word to fill in:")
    if st.session_state.available_words:
        cols = st.columns(len(st.session_state.available_words))
        for i, word in enumerate(st.session_state.available_words[:]):
            if cols[i].button(word, key=f"word_btn_{word}"):
                for idx in st.session_state.blank_indices:
                    if st.session_state.blank_answers[idx] == "":
                        st.session_state.blank_answers[idx] = word
                        break
                st.session_state.available_words.remove(word)

    # Check answers
    if st.button("Check Answers"):
        correct = True
        for idx in st.session_state.blank_indices:
            user = st.session_state.blank_answers[idx].lower().strip()
            answer = st.session_state.original_words[idx].strip(".,").lower()
            if user != answer:
                st.error(f"❌ `{user}` → Correct answer: `{answer}`")
                correct = Fal
