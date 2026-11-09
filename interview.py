import streamlit as st
import re
import random
from gemini_ai import evaluate_answer

# ==========================================
# Interview Questions
# ==========================================

questions = [

    # HR
    "Tell me about yourself.",
    "Why should we hire you?",
    "What are your strengths?",
    "What are your weaknesses?",
    "Where do you see yourself in 5 years?",
    "Why do you want to join our company?",
    "How do you handle pressure?",
    "Tell me about a challenging situation you faced?",
    "What motivates you?",
    "Describe your AI Placement Management System.",

    # Python
    "What is Python?",
    "Difference between List and Tuple?",
    "Difference between List and Dictionary?",
    "What is Exception Handling?",
    "What is File Handling?",
    "Explain OOP.",
    "Explain Inheritance.",
    "Explain Polymorphism.",
    "Explain Encapsulation.",
    "Explain Abstraction.",

    # Machine Learning
    "What is Machine Learning?",
    "Difference between AI and Machine Learning?",
    "Explain Decision Tree.",
    "Explain Random Forest.",
    "What is Supervised Learning?",
    "What is Unsupervised Learning?",
    "What is Deep Learning?",
    "What is Overfitting?",
    "What is Underfitting?",
    "What is Data Preprocessing?",

    # SQL
    "What is SQL?",
    "What is Primary Key?",
    "What is Foreign Key?",
    "What are SQL Joins?",
    "What is Normalization?",

    # Web
    "What is Streamlit?",
    "What is Flask?",
    "What is Git?",
    "What is GitHub?",
    "Explain REST API."

]
def interview_page():

    # ==========================
    # Session State
    # ==========================

    if "score" not in st.session_state:
        st.session_state.score = 0

    if "attempt" not in st.session_state:
        st.session_state.attempt = 0

    if "q_index" not in st.session_state:
        st.session_state.q_index = 0
    if "q_order" not in st.session_state:
        st.session_state.q_order = random.sample(
        range(len(questions)),
        len(questions)
    )
    if "time_left" not in st.session_state:
         st.session_state.time_left = 60

    # ==========================
    # Header
    # ==========================

    st.title("🎤 AI Interview Practice Portal")

    st.caption(
        "Practice Technical & HR Interview Questions with AI Evaluation"
    )

    total_questions = len(questions)

    current_number = st.session_state.q_index + 1

    st.progress(current_number / total_questions)

    st.markdown(
        f"### 📌 Question {current_number} of {total_questions}"
    )

    current_question = questions[
        st.session_state.q_index
    ]

    st.info(current_question)
    timer_placeholder = st.empty()

    timer_placeholder.warning(
    f"⏳ Time Remaining: {st.session_state.time_left} sec"
)
    # ==========================
    # Answer Box
    # ==========================

    answer = st.text_area(
        "✍ Your Answer",
        height=220,
        placeholder="Type your answer here...",
        key="answer_box"
    )

    col1, col2 = st.columns(2)
        # ==========================
    # Buttons
    # ==========================

    with col1:

        if st.button("✅ Evaluate", use_container_width=True):

            if answer.strip() == "":

                st.warning("⚠ Please enter your answer first.")

            else:

                try:

                    result = evaluate_answer(
                        current_question,
                        answer
                    )

                    score = 50

                    match = re.search(
                        r"Score\s*:\s*(\d+)",
                        result
                    )

                    if match:
                        score = int(match.group(1))

                    st.session_state.score += score
                    st.session_state.attempt += 1

                    st.success(f"✅ Score : {score}/100")

                    st.subheader("🤖 AI Feedback")

                    st.write(result)

                except Exception as e:

                    st.error(f"AI Error : {e}")

    with col2:

        if st.button("➡ Next Question", use_container_width=True):

            st.session_state.q_index += 1
            st.session_state.time_left = 60

            if st.session_state.q_index >= len(questions):

                st.session_state.q_index = 0

            st.rerun()

    # ==========================
    # Interview Summary
    # ==========================

    if st.session_state.attempt > 0:

        avg = (
            st.session_state.score
            /
            st.session_state.attempt
        )

        st.divider()

        st.subheader("📊 Interview Summary")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Questions Answered",
            st.session_state.attempt
        )

        c2.metric(
            "Total Score",
            st.session_state.score
        )

        c3.metric(
            "Average Score",
            f"{avg:.2f}%"
        )

        st.progress(avg / 100)

        if avg >= 80:
            st.success("🌟 Excellent Performance")

        elif avg >= 60:
            st.info("👍 Good Performance")

        elif avg >= 40:
            st.warning("🙂 Average Performance")

        else:
            st.error("⚠ Needs Improvement")

    # ==========================
    # Reset Interview
    # ==========================

    st.divider()

    if st.button("🔄 Reset Interview"):

        st.session_state.score = 0
        st.session_state.attempt = 0
        st.session_state.q_index = 0
        st.session_state.time_left = 60

        st.session_state.q_order = random.sample(
         range(len(questions)),
          len(questions)
)

        st.rerun()
            # ==========================================
    # Certificate Unlock
    # ==========================================

    if st.session_state.attempt > 0:

        avg = (
            st.session_state.score
            /
            st.session_state.attempt
        )

        if avg >= 70:

            username = st.session_state.get(
                "username",
                "Student"
            )

            st.divider()

            st.success("🏆 Congratulations! Certificate Unlocked")

            st.markdown(f"""
# 🏅 Certificate of Achievement

This is proudly presented to

## **{username}**

for successfully completing the

### **AI Interview Practice Module**

---

🎯 **Average Score:** **{avg:.2f}/100**

📅 **Status:** Completed Successfully

👏 Keep learning and all the best for your placements!

""")

        else:

            st.divider()

            st.info(
                "📌 Score at least 70% average to unlock the certificate."
            )