import streamlit as st
import pandas as pd
import pickle
import datetime
import os


# ============================
# Load ML Model
# ============================
model = pickle.load(open("model.pkl", "rb"))


# ============================
# Save Prediction History
# ============================
def save_history(username, data, result):

    file = "history.csv"

    new_data = pd.DataFrame([[
        username,
        data[0],
        data[1],
        data[2],
        data[3],
        result,
        str(datetime.datetime.now())
    ]], columns=[
        "username",
        "cgpa",
        "skills",
        "aptitude",
        "projects",
        "result",
        "date"
    ])

    if os.path.exists(file):

        try:
            df = pd.read_csv(file)

        except:

            df = pd.DataFrame(columns=new_data.columns)

        df = pd.concat([df, new_data], ignore_index=True)

    else:

        df = new_data

    df.to_csv(file, index=False)


# ============================
# Prediction Page
# ============================
def prediction_page():

    st.header("🎯 Placement Prediction")

    if "data" not in st.session_state:

        st.warning("Please enter student details first.")

        return

    data = pd.DataFrame(
        [st.session_state.data],
        columns=[
            "CGPA",
            "Skills",
            "Aptitude",
            "Projects",
            "Internship",
            "Communication",
            "Backlogs",
            "Hackathon"
        ]
    )

    probability = model.predict_proba(data)[0][1] * 100
    st.session_state.prediction = probability

    st.subheader(f"Placement Chance : {probability:.2f}%")

    st.progress(probability / 100)

    if probability >= 80:
        st.success("🔥 Excellent Placement Chance")

    elif probability >= 60:
        st.info("🙂 Good Placement Chance")

    elif probability >= 40:
        st.warning("⚠ Average Placement Chance")

    else:
        st.error("❌ Low Placement Chance")

    save_history(
        st.session_state.username,
        st.session_state.data,
        probability
    )