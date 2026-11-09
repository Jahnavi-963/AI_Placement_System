import pandas as pd
import os

FILE = "users.csv"

# ---------------- LOAD USERS ----------------
def load_users():
    if os.path.exists(FILE):
        df = pd.read_csv(FILE)

        # 🔥 CLEAN DATA (VERY IMPORTANT FIX)
        df["username"] = df["username"].astype(str).str.strip()
        df["password"] = df["password"].astype(str).str.strip()

        return df
    else:
        df = pd.DataFrame(columns=["username", "password"])
        df.to_csv(FILE, index=False)
        return df

# ---------------- SIGNUP ----------------
def signup(username, password):
    df = load_users()

    username = username.strip()
    password = password.strip()

    if username in df["username"].values:
        return False

    new_user = pd.DataFrame([[username, password]], columns=["username", "password"])
    df = pd.concat([df, new_user], ignore_index=True)
    df.to_csv(FILE, index=False)

    return True

# ---------------- LOGIN ----------------
def login(username, password):
    df = load_users()

    username = username.strip()
    password = password.strip()

    user = df[(df["username"] == username) & (df["password"] == password)]

    return not user.empty

# ---------------- FORGOT PASSWORD ----------------
def forgot(username):
    df = load_users()

    username = username.strip()

    user = df[df["username"] == username]

    if user.empty:
        return None

    return user.iloc[0]["password"]