import streamlit as st

st.title("Grammar")

# 탭 2개 만들기
tab1, tab2, tab3 = st.tabs(["Passive Voice", "Gerund", "Grammar quiz"])

with tab1:
    st.header("🧠 What is Passive Voice?")
    st.subheader("📌 Definition")
    st.markdown("""
    Passive voice is used when the subject **receives** the action instead of doing it.
    """)

    st.subheader("🔧 Structure")
    st.markdown("""
    `[Subject] + [form of "be"] + [past participle] (+ by [agent])`
    """)

    st.subheader("✅ Examples")
    st.markdown("""
    **Active:** The chef cooks the meal.  
    **Passive:** The meal is cooked (by the chef).  

    **Active:** They will finish the project.  
    **Passive:** The project will be finished (by them).
    """)

    st.subheader("🔍 Tips")
    st.markdown("""
    - Use passive voice when **who did the action** is unknown or unimportant.  
    - Focus is on the **result** or **object**, not the doer.
    """)

with tab2:
    st.header("🔁 What is a Gerund?")
    st.subheader("📌 Definition")
    st.markdown("""
    A gerund is the **-ing** form of a verb used as a **noun**.
    """)

    st.subheader("🔧 Structure")
    st.markdown("""
    `[Verb + ing]` = noun
    """)

    st.subheader("✅ Examples")
    st.markdown("""
    - Swimming is fun.  
    - I enjoy reading books.  
    - She is good at drawing.
    """)

    st.subheader("🔍 Tips")
    st.markdown("""
    - Gerunds can be **subjects**, **objects**, or come **after prepositions**.  
    - Some verbs are always followed by gerunds, like:  
      `enjoy`, `avoid`, `finish`, `consider`, `mind`, `suggest`, `keep`
    """)

with tab3:
    import streamlit as st
    active_sentence = "Tom eats an apple."
    correct_passive = ["An", "apple", "is", "eaten", "by", "Tom"]
    st.title("수동태 퀴즈")
    st.write("### 능동태 문장을 보고 수동태 문장을 완성하세요.")
    st.write(f"**능동태 문장:** {active_sentence}")
    word_buttons = ["An", "apple", "is", "eaten", "by", "Tom"]
    if "user_sentence" not in st.session_state:
    st.session_state.user_sentence = []
    cols = st.columns(len(word_buttons))
    for i, word in enumerate(word_buttons):
    if cols[i].button(word):
        st.session_state.user_sentence.append(word)
    st.write("#### 만든 문장:")
    st.write(" ".join(st.session_state.user_sentence))
    if st.button("제출"):
    if st.session_state.user_sentence == correct_passive:
        st.success("정답입니다! 🎉")
    if st.button("초기화"):
    st.session_state.user_sentence = []
    


