import streamlit as st
import numpy as np

# 퍼즐 정의
words = {
    'PYTHON': {'direction': 'across', 'row': 0, 'col': 0},
    'STREAMLIT': {'direction': 'down', 'row': 0, 'col': 2},
    'CODE': {'direction': 'across', 'row': 2, 'col': 1},
}

# 그리드 생성
grid_size = 10
grid = np.full((grid_size, grid_size), '', dtype=str)

# 단어를 그리드에 배치
for word, props in words.items():
    row, col = props['row'], props['col']
    if props['direction'] == 'across':
        grid[row, col:col+len(word)] = list(word)
    elif props['direction'] == 'down':
        grid[row:row+len(word), col] = list(word)

# 스트림릿을 사용하여 그리드 표시
st.title("가로세로 퍼즐")

for row in grid:
    st.text(' '.join([c if c else '_' for c in row]))

# 힌트 표시
st.subheader("Hints")
for word, props in words.items():
    direction = '가로' if props['direction'] == 'across' else '세로'
    st.write(f"{direction} - {word} ({props['row']+1}, {props['col']+1})")
