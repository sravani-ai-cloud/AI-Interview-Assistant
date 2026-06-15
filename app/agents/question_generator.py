from app.services.gemini_service import ask_gemini


def generate_questions(technology, level):

    prompt = f"""
    Generate 5 {level} level interview questions on {technology}.

    Return response in JSON format:

    {{
      "questions": [
        "question1",
        "question2",
        "question3",
        "question4",
        "question5"
      ]
    }}
    """

    return ask_gemini(prompt)