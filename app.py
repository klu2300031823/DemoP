import streamlit as st
from streamlit_autorefresh import st_autorefresh
import time

st.set_page_config(page_title="Aptitude Quiz", layout="centered")

TOTAL_TIME = 600

questions = [
{
"section":"Percentages",
"question":"A number is increased by 20% and becomes 240. What was the original number?",
"type":"mcq",
"options":["180","190","200","220"],
"answer":"200"
},
{
"section":"Profit & Loss",
"question":"A shopkeeper buys an item for ₹800 and sells it for ₹920. Profit percentage?",
"type":"mcq",
"options":["12%","15%","18%","20%"],
"answer":"15%"
},
{
"section":"Ages",
"question":"Father is 4 times his son's age. After 10 years, father will be twice the son's age. Present son's age?",
"type":"mcq",
"options":["8","10","12","14"],
"answer":"10"
},
{
"section":"Probability",
"question":"A die is thrown. Probability of getting a multiple of 3?",
"type":"mcq",
"options":["1/6","1/3","1/2","2/3"],
"answer":"1/3"
},
{
"section":"Time & Work",
"question":"A can finish work in 12 days and B in 18 days. Together they finish in how many days?",
"type":"mcq",
"options":["6.2","7.2","8.5","9"],
"answer":"7.2"
},
{
"section":"Ratio",
"question":"Ratio of boys to girls is 3:2. Total students are 50. Number of girls?",
"type":"mcq",
"options":["20","25","30","35"],
"answer":"20"
},
{
"section":"Simple Interest",
"question":"SI on ₹5000 at 8% for 2 years?",
"type":"mcq",
"options":["700","750","800","850"],
"answer":"800"
},
{
"section":"Compound Interest",
"question":"CI on ₹1000 at 10% for 2 years?",
"type":"mcq",
"options":["200","210","220","230"],
"answer":"210"
},
{
"section":"Average",
"question":"Average of 10,20,30,40,50?",
"type":"mcq",
"options":["25","30","35","40"],
"answer":"30"
},
{
"section":"Speed Distance Time",
"question":"A car travels 180 km in 3 hours. Find speed.",
"type":"mcq",
"options":["50","55","60","65"],
"answer":"60"
},
{
"section":"Number Series",
"question":"2, 6, 12, 20, 30, ?",
"type":"mcq",
"options":["36","40","42","44"],
"answer":"42"
},
{
"section":"Boats & Streams",
"question":"Boat speed is 12 km/hr and stream speed is 3 km/hr. Downstream speed?",
"type":"mcq",
"options":["9","12","15","18"],
"answer":"15"
},
{
"section":"Mensuration",
"question":"Area of a circle with radius 7. Use π = 22/7. Enter integer answer only.",
"type":"text",
"answer":"154"
},
{
"section":"Probability",
"question":"A bag contains 3 red and 2 blue balls. Probability of drawing a red ball. Enter decimal up to 2 places (Example: 0.60)",
"type":"text",
"answer":"0.60"
}
]

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

if "current" not in st.session_state:
    st.session_state.current = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "submitted" not in st.session_state:
    st.session_state.submitted = False

st_autorefresh(interval=1000,key="timer")

elapsed = int(time.time() - st.session_state.start_time)
remaining = TOTAL_TIME - elapsed

if remaining <= 0:
    st.session_state.submitted = True
    remaining = 0

mins = remaining // 60
secs = remaining % 60

st.title("🧠 Aptitude Quiz")
st.markdown(f"### ⏳ Time Left: {mins:02d}:{secs:02d}")

if not st.session_state.submitted:

    qno = st.session_state.current
    q = questions[qno]

    progress = (qno + 1) / len(questions)
    st.progress(progress)

    st.subheader(f"Question {qno+1} / {len(questions)}")
    st.write(q["question"])
    if q["type"] == "mcq":
    
            selected = st.radio(
                "Choose One",
                q["options"],
                index=None,
                key=f"q_{qno}"
            )

        if selected:
            st.session_state.answers[qno] = selected

    else:

        txt = st.text_input(
            "Enter Answer",
            value=st.session_state. answers.get(qno,""),
            key=f"text_{qno}"
        )

        st.session_state.answers[qno] = txt

    c1,c2,c3 = st.columns(3)

    if qno == 0:

        with c3:
            if st.button("Next"):
                st.session_state.current += 1
                st.rerun()

    elif qno == len(questions)-1:

        with c1:
            if st.button("Previous"):
                st.session_state.current -= 1
                st.rerun()

        with c3:
            if st.button("Submit"):
                st.session_state.submitted = True
                st.rerun()

    else:

        with c1:
            if st.button("Previous"):
                st.session_state.current -= 1
                st.rerun()

        with c3:
            if st.button("Next"):
                st.session_state.current += 1
                st.rerun()

else:

    st.title("📊 Results")

    score = 0
    section_stats = {}

    for i,q in enumerate(questions):

        user = st.session_state.answers.get(i,"Not Answered")
        correct = q["answer"]

        result = "❌"

        if str(user).strip().lower() == str(correct).strip().lower():
            score += 1
            result = "✅"

        sec = q["section"]

        if sec not in section_stats:
            section_stats[sec] = [0,0]

        section_stats[sec][1] += 1

        if result == "✅":
            section_stats[sec][0] += 1

        st.markdown("---")
        st.write(f"### Question {i+1}")
        st.write(q["question"])
        st.write(f"Your Answer: {user}")
        st.write(f"Correct Answer: {correct}")
        st.write(f"Result: {result}")

    percentage = round(score*100/len(questions),2)

    st.markdown("---")
    st.success(f"Score : {score}/{len(questions)}")
    st.success(f"Percentage : {percentage}%")

    strong = []
    weak = []

    for sec,val in section_stats.items():

        correct,total = val

        if correct/total >= 0.5:
            strong.append(sec)
        else:
            weak.append(sec)

    st.subheader("💪 Strong Performance")

    if strong:
        for i in strong:
            st.write("✅",i)
    else:
        st.write("None")

    st.subheader("📚 Areas To Improve")

    if weak:
        for i in weak:
            st.write("❌",i)
    else:
        st.write("None")

    st.subheader("📝 Overall Analysis")

    if percentage >= 80:
        st.success("Excellent aptitude skills.")
    elif percentage >= 60:
        st.info("Good performance. Keep practicing.")
    elif percentage >= 40:
        st.warning("Average performance. More practice needed.")
    else:
        st.error("Needs significant improvement.")
