import streamlit as st
import pandas as pd
import plotly.express as px
import os

def dashboard_page():

    st.title("📊 Placement Dashboard")

    st.caption("AI Powered Student Analytics")

    st.divider()

    st.success(f"👋 Welcome, {st.session_state.username}")

    # ==========================
    # Dashboard Metrics
    # ==========================

    c1, c2, c3, c4 = st.columns(4)

    ats = st.session_state.get("ats_score", 0)
    interviews = st.session_state.get("attempt", 0)
    interview_score = st.session_state.get("score", 0)

    if interviews > 0:
        avg = interview_score / interviews
    else:
        avg = 0

    with c1:
        st.metric(
            "📄 ATS Score",
            ats
        )

    with c2:
        st.metric(
            "🎤 Interviews",
            interviews
        )

    with c3:
        st.metric(
            "⭐ Avg Interview",
            f"{avg:.1f}%"
        )

    with c4:
        st.metric(
            "🎯 Placement Chance",
            "85%"
        )

    st.divider()

    # ==========================
    # Graph Data
    # ==========================

    df = pd.DataFrame({

        "Skills":[2,4,6,8,10],

        "Placement":[20,35,55,80,95],

        "CGPA":[5,6,7,8,9]

    })

    left,right = st.columns(2)

    with left:

        fig = px.line(

            df,

            x="Skills",

            y="Placement",

            markers=True,

            title="📈 Skills vs Placement"

        )

        st.plotly_chart(fig,use_container_width=True)

    with right:

        fig2 = px.bar(

            df,

            x="CGPA",

            y="Placement",

            title="📊 CGPA vs Placement",

            color="Placement"

        )

        st.plotly_chart(fig2,use_container_width=True)

    st.divider()
        # =====================================
    # Last 5 Predictions
    # =====================================

    if os.path.exists("history.csv"):

        history = pd.read_csv("history.csv")

        user_history = history[
            history["username"] == st.session_state.username
        ]

        if len(user_history) > 0:

            st.subheader("📋 Recent Prediction History")

            last5 = user_history.sort_values(
                by="date",
                ascending=False
            ).head(5)

            st.dataframe(last5, use_container_width=True)

            st.divider()

            latest_score = float(last5.iloc[0]["result"])
            average_score = float(user_history["result"].mean())
            total_predictions = len(user_history)

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric(
                    "📌 Total Predictions",
                    total_predictions
                )

            with c2:
                st.metric(
                    "🎯 Latest Score",
                    f"{latest_score:.2f}%"
                )

            with c3:
                st.metric(
                    "📊 Average Score",
                    f"{average_score:.2f}%"
                )

        else:

            st.info("No Prediction History Available.")

    else:

        st.warning("history.csv file not found.")

    st.divider()

    # =====================================
    # Strengths & Improvements
    # =====================================

    left, right = st.columns(2)

    with left:

        st.subheader("🏆 Your Strengths")

        st.success("✅ Python")

        st.success("✅ Machine Learning")

        st.success("✅ Streamlit")

        st.success("✅ Project Development")

    with right:

        st.subheader("⚠ Areas to Improve")

        st.warning("📌 DSA")

        st.warning("📌 SQL")

        st.warning("📌 Aptitude")

        st.warning("📌 Communication")

    st.divider()

        # =====================================
    # Career Progress
    # =====================================

    st.divider()

    st.subheader("🎯 Career Progress")

    if avg >= 80:

        st.success("🟢 Placement Ready")

        st.progress(0.90)

        st.write("""
✔ Excellent Interview Performance

✔ Resume is Competitive

✔ Start Applying for Companies

✔ Participate in Coding Contests
""")

    elif avg >= 60:

        st.info("🟡 Intermediate Level")

        st.progress(0.70)

        st.write("""
✔ Improve DSA

✔ Practice SQL

✔ Attend More Mock Interviews

✔ Increase ATS Score
""")

    else:

        st.warning("🔴 Beginner Level")

        st.progress(0.40)

        st.write("""
✔ Learn Python & DSA

✔ Improve Resume

✔ Build More Projects

✔ Practice Aptitude Daily
""")