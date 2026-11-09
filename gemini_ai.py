import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=API_KEY)


def evaluate_answer(question, answer):

    prompt = f"""
You are an expert technical interviewer.

Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer.

Give output exactly in this format:

Score: <number out of 100>

Feedback:
<2-3 lines>

Strength:
<one line>

Improvement:
<one line>
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"""
Score: 50

Feedback:
Gemini API Error.

Strength:
Unable to evaluate.

Improvement:
Check API Key or Internet.

Error:
{e}
"""