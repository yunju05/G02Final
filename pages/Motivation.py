import streamlit as st

st.write("# Motivation")

url="https://github.com/yunju05/G02Final/raw/main/images/%EB%94%94%EB%A6%AC%20text%20picture.png"
st.image(url)
url1="https://github.com/yunju05/G02Final/raw/main/images/%EB%94%94%EB%A6%AC%20%EC%9B%8C%EB%93%9C%20%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C.png"
st.image(url1)
st.write("### Let's guess the content of this story and share it!")
    
st.subheader("📓 Guess Notebook")

# Initialize session state
if "guess_notes" not in st.session_state:
    st.session_state.guess_notes = []

# Form to add new guesses
with st.form("guess_form", clear_on_submit=True):
    new_guess = st.text_area("💭 Add a new guess or theory:", height=100)
    submitted = st.form_submit_button("➕ Add")

    if submitted and new_guess.strip():
        st.session_state.guess_notes.append(new_guess.strip())
        st.success("Guess added!")

# Display saved guesses
st.markdown("---")
if st.session_state.guess_notes:
    for i, guess in enumerate(reversed(st.session_state.guess_notes), 1):
        st.markdown(f"**{len(st.session_state.guess_notes) - i + 1}.** {guess}")
else:
    st.info("No guesses yet. Start writing!")

# Clear guesses option
with st.expander("⚙️ Clear all guesses"):
    if st.button("🗑️ Delete All Guesses", key="delete_guesses"):
        st.session_state.guess_notes = []
        st.success("All guesses cleared.")

st.write("### Let's listen to the story!")

