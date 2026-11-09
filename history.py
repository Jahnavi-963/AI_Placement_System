import streamlit as st
import pandas as pd
import os

def history_page():

    st.header("📈 Prediction History")

    if not os.path.exists("history.csv"):
        st.warning("No Prediction History Found.")
        return

    history = pd.read_csv("history.csv")

    # Debug
    st.write("Total Records:", len(history))

    if history.empty:
        st.warning("No Prediction History Found.")
        return

    username = st.session_state.get("username", "")

    user_history = history[
        history["username"].astype(str).str.strip().str.lower()
        ==
        username.strip().lower()
    ]

    if user_history.empty:
        st.warning("No Prediction History Found for this user.")
    else:
        st.dataframe(user_history, use_container_width=True)