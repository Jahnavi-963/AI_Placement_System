import streamlit as st


def feedback_page():

    st.header("🎤 AI Interview Feedback Dashboard")

    if st.session_state.get("attempt", 0) == 0:
        st.warning("⚠ Please complete at least one interview first.")
        return

    attempts = st.session_state.get("attempt", 0)
    total_score = st.session_state.get("score", 0)

    average = total_score / attempts

    st.metric("Average Interview Score", f"{average:.2f}%")

    st.progress(average / 100)

    # ==========================================
    # PERFORMANCE LEVEL
    # ==========================================

    if average >= 80:
        st.success("🌟 Excellent Performance")
    elif average >= 60:
        st.info("👍 Good Performance")
    elif average >= 40:
        st.warning("🙂 Average Performance")
    else:
        st.error("⚠ Needs Improvement")

    st.divider()

    st.subheader("💪 Strengths")

    strengths = []

    if average >= 80:
        strengths = [
            "Excellent Communication",
            "Good Technical Knowledge",
            "Confidence",
            "Problem Solving"
        ]

    elif average >= 60:
        strengths = [
            "Communication",
            "Basic Programming",
            "Positive Attitude"
        ]

    else:
        strengths = [
            "Willingness to Learn"
        ]

    for item in strengths:
        st.success("✅ " + item)

    st.divider()

    st.subheader("📉 Areas to Improve")
    weaknesses = []

    if average >= 80:
        weaknesses = [
            "Advanced DSA",
            "System Design",
            "Competitive Coding"
        ]

    elif average >= 60:
        weaknesses = [
            "Data Structures",
            "SQL",
            "DBMS",
            "Operating Systems"
        ]

    else:
        weaknesses = [
            "Python Basics",
            "C++",
            "DSA",
            "SQL",
            "Communication Skills"
        ]

    st.write(weaknesses)

    for item in weaknesses:
     st.write(item)
     st.divider()

    # ==========================================
    # RECOMMENDED TOPICS
    # ==========================================

    st.subheader("📚 Recommended Topics")

    topics = [
        "Arrays & Strings",
        "Linked Lists",
        "Stacks & Queues",
        "Trees",
        "SQL Joins",
        "DBMS",
        "Operating Systems",
        "Computer Networks",
        "OOP Concepts",
        "HR Interview Questions"
    ]

    for topic in topics:
        st.write("📖", topic)

    st.divider()

    # ==========================================
    # 7-DAY IMPROVEMENT PLAN
    # ==========================================

    st.subheader("📅 7-Day Improvement Plan")

    plan = {
        "Day 1": "Python Revision + Coding Practice",
        "Day 2": "Arrays & Strings",
        "Day 3": "Linked Lists + Stack + Queue",
        "Day 4": "SQL + DBMS",
        "Day 5": "Operating Systems + CN",
        "Day 6": "Mock Interview + HR Questions",
        "Day 7": "Complete Revision + Projects"
    }

    for day, task in plan.items():
        st.info(f"**{day}** → {task}")

    st.divider()

    # ==========================================
    # FINAL RECOMMENDATION
    # ==========================================

    st.subheader("🚀 Final Recommendation")

    if average >= 80:
        st.success(
            "🔥 You are placement ready! Continue mock interviews and apply to product & service-based companies."
        )

    elif average >= 60:
        st.warning(
            "🙂 Good progress. Strengthen DSA, DBMS and SQL to improve interview performance."
        )

    else:
        st.error(
            "⚠ Focus on programming fundamentals, aptitude, communication, and regular mock interviews."
        )