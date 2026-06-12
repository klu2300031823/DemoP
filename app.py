import streamlit as st

st.set_page_config(page_title="Aptitude MCQ Quiz")

st.title("📝 Aptitude MCQ Quiz")

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
        "q": "Next number: 2, 4, 6, 8, ?",
        "options": ["9", "10", "11", "12"],
        "answer": "10"
    },
    {
        "q": "If today is Monday, after 3 days it is?",
        "options": ["Tuesday", "Wednesday", "Thursday", "Friday"],
        "answer": "Thursday"
    },
    {
        "q": "25% of 200 = ?",
        "options": ["25", "50", "75", "100"],
        "answer": "50"
    },
    {
        "q": "A pen costs ₹5. Cost of 4 pens?",
        "options": ["15", "20", "25", "30"],
        "answer": "20"
    },
    {
        "q": "60 km/hr for 2 hours = ? km",
        "options": ["100", "110", "120", "130"],
        "answer": "120"
    }
]

user_answers = []

for i, q in enumerate(questions):
    ans = st.radio(
        f"Q{i+1}. {q['q']}",
        q["options"],
        key=i
    )
    user_answers.append(ans)

if st.button("Submit"):
    score = 0

    for i, q in enumerate(questions):
        if user_answers[i] == q["answer"]:
            score += 1

    st.success(f"🎯 Score: {score}/10")

    st.subheader("Correct Answers")
    for i, q in enumerate(questions):
        st.write(f"Q{i+1}: {q['answer']}")
