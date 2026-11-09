import pandas as pd
import os

FILE = "profiles.csv"

# Create file if it doesn't exist
if not os.path.exists(FILE):
    df = pd.DataFrame(columns=[
        "username",
        "name",
        "email",
        "college",
        "branch",
        "year",
        "roll_no",
        "phone",
        "skills"
    ])
    df.to_csv(FILE, index=False)


# Save Profile
def save_profile(username, name, email, college, branch, year, roll_no, phone, skills):

    df = pd.read_csv(FILE)

    # Remove old profile if it exists
    df = df[df["username"] != username]

    new_row = pd.DataFrame([{
        "username": username,
        "name": name,
        "email": email,
        "college": college,
        "branch": branch,
        "year": year,
        "roll_no": roll_no,
        "phone": phone,
        "skills": skills
    }])

    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(FILE, index=False)


# Load Profile
def load_profile(username):

    df = pd.read_csv(FILE)

    user = df[df["username"] == username]

    if len(user) == 0:
        return None

    return user.iloc[0]