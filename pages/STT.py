import streamlit as st

# 오디오 데이터를 처리할 백엔드가 있다고 가정한 예시
st.markdown("""
    <h2>음성 인식 예제</h2>
    <p>녹음을 시작하려면 버튼을 누르세요:</p>
    <button id="recordButton">녹음</button>
    <p id="status"></p>
    <script>
        const recordButton = document.getElementById('recordButton');
        const status = document.getElementById('status');
        
        recordButton.addEventListener('click', () => {
            // 여기에 녹음 기능 구현
            // 오디오 데이터를 서버로 전송하여 STT 처리
            status.textContent = '녹음 중...';
            // 녹음 후
            status.textContent = '처리 중...';
            // 처리 완료 후
            status.textContent = '완료!';
        });
    </script>
""", unsafe_allow_html=True)
