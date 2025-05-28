import streamlit as st

st.title("Grammar")

# 탭 4개 만들기
tab1, tab2, tab3, tab4 = st.tabs(["Passive Voice", "관계대명사", "동명사", "activity"])

with tab1:
    st.header("🧠 What is Passive Voice?")
  import streamlit as st

st.title("📘 Passive Voice - Easy Grammar Guide")
st.markdown("### 🧠 What is Passive Voice?")

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
    st.header("🔁 ")
  
with tab3:
    st.header("🧩")
  

with tab4:
    st.header("📊 ")
    
