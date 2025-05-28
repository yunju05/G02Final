import streamlit as st
import numpy as np

# CSS 스타일 정의
st.markdown("""
    <style>
    .grid-container {
        display: grid;
        grid-template-columns: repeat(10, 1fr);
        grid-gap: 2px; /* 셀 간의 간격 */
    }
    .grid-item {
        text-align: center;
        padding: 5px; /* 셀 내부 여백 */
        border: 1px solid #ccc; /* 셀 경계선 */
    }
    .input-item {
        width: 100%;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 퍼즐 정의
words = {
    'PYTHON': {'direction': 'across', 'row': 1, 'col': 0},
    'STREAMLIT': {'direction': 'down', 'row': 0, 'col': 2},
    'CODE': {'direction': 'down', 'row': 0, 'col': 4},
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

user_grid = np.full((grid_size, grid_size), '', dtype=str)

# 사용자 입력을 위한 그리드 출력
st.markdown('<div class="grid-container">', unsafe_allow_html=True)
for row_index in range(grid_size):
    for col_index in range(grid_size):
        if grid[row_index, col_index] != '':
            user_input = st.text_input("", "", max_chars=1, key=f"{row_index}-{col_index}")
            user_grid[row_index, col_index] = user_input.upper()
            st.markdown(f'<div class="grid-item input-item">{user_input.upper()}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="grid-item"></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 제출 버튼
if st.button("Submit"):
    # 정답과 비교
    correct = True
    for row_index in range(grid_size):
        for col_index in range(grid_size):
            if grid[row_index, col_index] != '' and grid[row_index, col_index] != user_grid[row_index, col_index]:
                correct = False
    if correct:
        st.success("정답입니다!")
    else:
        st.error("틀렸습니다. 다시 시도해보세요.")

# 힌트 표시
st.subheader("Hints")
for word, props in words.items():
    direction = '가로' if props['direction'] == 'across' else '세로'
    st.write(f"{direction} - {word} ({props['row']+1}, {props['col']+1})")
