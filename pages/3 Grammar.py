import streamlit as st

st.title("Grammar")

# 탭 4개 만들기
tab1, tab2, tab3, tab4 = st.tabs(["Passive Voice", "관계대명사", "동명사", "activity"])

with tab1:
    st.header("🧠 What is Passive Voice?")
    st.markdown("""
    In English, we can say a sentence in two ways:

    1. **Active Voice** – The subject **does** something.  
    2. **Passive Voice** – Something **is done** to the subject.
    """)

    st.markdown("### 🔹 Active Voice Example:")
    st.code("The cat eats the fish.", language='text')
    st.markdown("➡️ The **cat** is doing the action (eats).")

    st.markdown("### 🔹 Passive Voice Example:")
    st.code("The fish is eaten by the cat.", language='text')
    st.markdown("➡️ The **fish** receives the action (is eaten).")

    st.markdown("### ✅ How to make Passive Voice:")
    st.markdown("**be + past participle (p.p)**\n\nExample: `is eaten`, `was cleaned`, `will be built`")

    st.markdown("### 🕒 Passive Voice by Tense:")

    st.table({
        "Tense": ["Present", "Past", "Future"],
        "Active": ["He cleans the room.", "She washed the car.", "They will build a house."],
        "Passive": ["The room is cleaned.", "The car was washed.", "A house will be built."]
    })

    st.markdown("### 💡 Tips:")
    st.markdown("""
    - Use passive voice with **action verbs**.
    - Use passive voice when the action is more important than the person doing it.
    """)

    st.success("Now you understand Passive Voice! 🎉")

with tab2:
    st.header("🔁 관계대명사 탭 내용 작성하세요")

with tab3:
    st.header("🧩 동명사 탭 내용 작성하세요")

with tab4:
    st.header("📊 activity 탭 내용 작성하세요")

st.title("Learn Passive Voice with a Story!")

# 이야기 문장 리스트
active_sentences = [
    "Leo and his friends discovered a path leading to the Whispering Woods.",
    "The locals avoided it, saying it was bewitched.",
    "The adventurous teens couldn’t resist exploring.",
    "The trees started whispering.",
    "Each tree told stories of ancient times.",
    "The trees warned them about the dangers of forgetting the past.",
    "The friends promised to protect the woods.",
    "They left the woods wiser, ready to advocate for its preservation."
]

# 각 문장에 대응하는 수동태 문장 (간단한 예)
passive_sentences = [
    "A path leading to the Whispering Woods was discovered by Leo and his friends.",
    "It was avoided by the locals, saying it was bewitched.",
    "Exploring couldn’t be resisted by the adventurous teens.",
    "Whispering was started by the trees.",
    "Stories of ancient times were told by each tree.",
    "They were warned about the dangers of forgetting the past by the trees.",
    "A promise to protect the woods was made by the friends.",
    "The woods were left wiser by them, ready to advocate for its preservation."
]

st.markdown("### 📖 Story in Active Voice:")
for i, sentence in enumerate(active_sentences):
    st.write(f"{i+1}. {sentence}")

st.markdown("---")
st.markdown("### 🌀 Same Story in Passive Voice:")
for i, sentence in enumerate(passive_sentences):
    st.write(f"{i+1}. {sentence}")

st.markdown("---")
st.markdown("### 🎯 Interactive Quiz: Choose the correct passive sentence for the active sentence below!")

# 퀴즈용 문장 랜덤 선택
quiz_idx = st.session_state.get('quiz_idx', random.randint(0, len(active_sentences)-1))
st.session_state['quiz_idx'] = quiz_idx

st.write(f"**Active:** {active_sentences[quiz_idx]}")

# 선택지 섞기
options = passive_sentences.copy()
random.shuffle(options)

# 라디오 버튼으로 선택
user_answer = st.radio("Choose the correct passive voice sentence:", options)

# 정답 확인
if st.button("Check Answer"):
    if user_answer == passive_sentences[quiz_idx]:
        st.success("Correct! Well done! 🎉")
    else:
        st.error("Oops, that's not correct. Try again!")

st.markdown("---")
st.markdown("### 💡 Passive Voice Tip:")
st.write("Passive voice is formed by **be + past participle**. It emphasizes the action or the receiver of the action, not the doer.")

