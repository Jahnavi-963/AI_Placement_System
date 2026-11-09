import PyPDF2

def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


def ats_score(text):
    keywords = [
        "Python", "Machine Learning", "AI", "Data Science",
        "Project", "SQL", "Git", "C++", "Java"
    ]

    score = 0

    for word in keywords:
        if word.lower() in text.lower():
            score += 10

    return min(score, 100)


def suggestions(score):
    if score > 70:
        return "🔥 Strong Resume"
    elif score > 40:
        return "⚠ Improve keywords and add projects"
    else:
        return "❌ Weak Resume - Add skills + projects"