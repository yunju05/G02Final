import streamlit as st

# 퀴즈 데이터는 여기에 쏙!
questions_data = [
    {
        "question": "Leo and his friends decided to explore the Whispering Woods because they were known for their beautiful scenery.",
        "answer": "X"
    },
    {
        "question": "The Whispering Woods were avoided by locals due to the belief that they were bewitched.",
        "answer": "O"
    },
    {
        "question": "As the group ventured deeper into the woods, they encountered trees that could talk and share stories.",
        "answer": "O"
    },
    {
        "question": "The trees only told stories about happy endings and celebrations.",
        "answer": "X"
    },
    {
        "question": "After leaving the woods, Leo and his friends felt a stronger commitment to protecting nature.",
        "answer": "O"
    }
]

# 퀴즈 상태를 저장할 공간을 만들어줘요 (세션 스테이트!)
if 'current_question_index' not in st.session_state:
    st.session_state.current_question_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'feedback_message' not in st.session_state:
    st.session_state.feedback_message = ""

# 퀴즈 시작 함수
def start_quiz():
    st.session_state.quiz_started = True
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.feedback_message = ""

# 정답 확인 함수
def check_answer(user_answer):
    current_q = questions_data[st.session_state.current_question_index]
    correct_answer = current_q["answer"]

    if user_answer == correct_answer:
        st.session_state.score += 1
        st.session_state.feedback_message = "🎉 정답! 정말 똑똑하시네요! 🎉"
    else:
        st.session_state.feedback_message = f"😅 아쉽지만 오답이에요! 정답은 '{correct_answer}'였답니다."

    # 다음 문제로 넘어가기 전에 잠시 기다려줘요
    st.session_state.current_question_index += 1

# 퀴즈 앱의 제목!
st.title("🌳 속삭이는 숲 OX 퀴즈! 🌳")
st.write("레오와 친구들의 신비한 숲 탐험 이야기를 OX 퀴즈로 풀어봐요!")

if not st.session_state.quiz_started:
    st.write("퀴즈를 시작하려면 아래 버튼을 눌러주세요!")
    if st.button("✨ 퀴즈 시작! ✨"):
        start_quiz()
else:
    # 모든 문제를 다 풀었는지 확인해요
    if st.session_state.current_question_index < len(questions_data):
        current_q = questions_data[st.session_state.current_question_index]

        st.subheader(f"문제 {st.session_state.current_question_index + 1}. 다음 문장이 맞으면 O, 틀리면 X를 선택하세요.")
        st.write(f"**{current_q['question']}**")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("⭕ O", use_container_width=True):
                check_answer("O")
        with col2:
            if st.button("❌ X", use_container_width=True):
                check_answer("X")

        # 피드백 메시지 보여주기
        if st.session_state.feedback_message:
            st.info(st.session_state.feedback_message)
            # 다음 문제로 넘어가기 위해 피드백 메시지를 초기화
            # (이 부분은 사용자가 다음 문제를 볼 준비가 되었을 때만 지우는 게 좋아요)
            # 여기서는 버튼 클릭 후 바로 다음 문제로 넘어가므로, 메시지가 잠시 보였다가 사라집니다.
            # 만약 메시지를 더 오래 보고 싶다면, 다른 로직이 필요해요!
            # st.session_state.feedback_message = "" # 이 줄을 주석 처리하면 메시지가 계속 남아있어요.

    else:
        st.balloons() # 퀴즈가 끝나면 풍선이 팡팡!
        st.subheader("🎉 퀴즈 끝! 🎉")
        st.write(f"총 {len(questions_data)}문제 중 {st.session_state.score}문제를 맞히셨어요!")

        if st.session_state.score == len(questions_data):
            st.success("와우! 모든 문제를 다 맞히셨네요! 숲의 비밀을 모두 아시는군요! 🤩")
        elif st.session_state.score >= len(questions_data) / 2:
            st.info("잘하셨어요! 숲의 이야기에 대해 많이 배우셨네요! 👍")
        else:
            st.warning("조금 더 노력하면 숲의 비밀을 모두 풀 수 있을 거예요! 🧐")

        if st.button("🔄 퀴즈 다시 시작하기"):
            start_quiz()

# 퀴즈 관련 정보 더 찾아보기
st.markdown("---")
st.write("혹시 파이썬 퀴즈 만들기에 대해 더 궁금한 점이 있으신가요?")
st.write("아래 자료들을 참고해 보세요!")
st.markdown("""
- 파이썬 함수 퀴즈: [[1]](https://pynative.com/python-functions-quiz/)
- 파이썬 객관식 문제: [[5]](https://www.ccbp.in/blog/articles/python-mcqs)
- 스트림릿으로 퀴즈 페이지 만들기: [[7]](https://myun9-cloud.tistory.com/24)
""")
