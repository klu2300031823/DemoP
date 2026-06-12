import streamlit as st
import time

st.set_page_config(page_title="Aptitude Quiz")

questions = [
    {
        "q": "10 + 15 = ?",
        "options": ["20", "25", "30", "35"],
        "answer": "25"
    },
    {
        "q": "20 - 8 = ?",
        "options": ["10", "12", "14", "16"],
        "answer": "12"
    },
    {
        "q": "6 × 4 = ?",
        "options": ["20", "22", "24", "26"],
        "answer": "24"
    },
    {
        "q": "36 ÷ 6 = ?",
        "options": ["4", "5", "6", "7"],
        "answer": "6"
    },
    {
        "q": "50% of 100 = ?",
        "options": ["25", "50", "75", "100"],
        "answer": "50"
    },
    {
        "q": "Next number: 2,4,6,8,?",
        "options": ["9", "10", "11", "12"],
        "answer": "10"
    },
    {
        "q": "Monday + 3 days = ?",
        "options": ["Tuesday", "Wednesday", "Thursday", "Friday"],
        "answer": "Thursday"
    },
    {
        "q": "25% of 200 = ?",
        "options": ["25", "50", "75", "100"],
        "answer": "50"
    },
    {
        "q": "Cost of 4 pens if 1 pen costs ₹5?",
        "options": ["15", "20", "25", "30"],
        "answer": "20"
    },
    {
        "q": "60 km/hr for 2 hours = ?",
        "options": ["100", "110", "120", "130"],
        "answer": "120"
    }
]

if "current" not in st.session_state:
    st.session_state.current = 0
    st.session_state.answers = {}
    st.session_state.start_time = time.time()
    st.session_state.finished = False

st.title("📝 Aptitude Quiz")

# 2 minute timer
remaining = 120 - int(time.time() - st.session_state.start_time)

if remaining <= 0:
    st.session_state.finished = True

if not st.session_state.finished:

    st.warning(f"⏳ Time Left: {remaining} seconds")

    q = questions[st.session_state.current]

    st.subheader(
        f"Question {st.session_state.current + 1}/{len(questions)}"
    )

    choice = st.radio(
        q["q"],
        q["options"],
        key=f"q{st.session_state.current}"
    )

    st.session_state.answers[st.session_state.current] = choice

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Previous") and st.session_state.current > 0:
            st.session_state.current -= 1
            st.rerun()

    with col2:
        if st.session_state.current < len(questions) - 1:
            if st.button("Next ➡"):
                st.session_state.current += 1
                st.rerun()
        else:
            if st.button("Submit"):
                st.session_state.finished = True
                st.rerun()

else:
    score = 0

    for i, q in enumerate(questions):
        if st.session_state.answers.get(i) == q["answer"]:
            score += 1

    st.success(f"🎯 Final Score: {score}/{len(questions)}")

    st.subheader("Correct Answers")

    for i, q in enumerate(questions):
        st.write(
            f"Q{i+1}. {q['q']} → ✅ {q['answer']}"
        )
