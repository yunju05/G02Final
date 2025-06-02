import streamlit as st
import numpy as np

# CSS to adjust the spacing between input fields
st.markdown("""
    <style>
    .block-container {
        padding: 0px;
    }
    .stTextInput>div {
        margin: 0px; /* Remove margin */
    }
    .stTextInput>div>input {
        padding: 5px; /* Adjust padding for the input */
        text-align: center; /* Center align text */
    }
    </style>
""", unsafe_allow_html=True)

words = {
    'PYTHON': {'direction': 'across', 'row': 1, 'col': 0},
    'STREAMLIT': {'direction': 'down', 'row': 0, 'col': 2},
    'CODE': {'direction': 'down', 'row': 0, 'col': 4},
}

grid_size = 10
grid = np.full((grid_size, grid_size), '', dtype=str)

for word, props in words.items():
    row, col = props['row'], props['col']
    if props['direction'] == 'across':
        grid[row, col:col+len(word)] = list(word)
    elif props['direction'] == 'down':
        grid[row:row+len(word), col] = list(word)

st.title("가로세로 퍼즐")

user_grid = np.full((grid_size, grid_size), '', dtype=str)

for row_index in range(grid_size):
    cols = st.columns(grid_size)
    for col_index in range(grid_size):
        if grid[row_index, col_index] != '':
            user_input = cols[col_index].text_input("", "", max_chars=1, key=f"{row_index}-{col_index}")
            user_grid[row_index, col_index] = user_input.upper()

if st.button("Submit"):
    correct = True
    for row_index in range(grid_size):
        for col_index in range(grid_size):
            if grid[row_index, col_index] != '' and grid[row_index, col_index] != user_grid[row_index, col_index]:
                correct = False
    if correct:
        st.success("정답입니다!")
    else:
        st.error("틀렸습니다. 다시 시도해보세요.")

st.subheader("Hints")
for word, props in words.items():
    direction = '가로' if props['direction'] == 'across' else '세로'
    st.write(f"{direction} - {word} ({props['row']+1}, {props['col']+1})")
