from app.services.gemini_service import ask_gemini


def generate_interview(technology, level):

    prompt = f"""
    Generate 5 {level} level interview questions on {technology}.

    For each question provide:

    1. Question
    2. Answer
    3. Difficulty

    Return response in JSON format only.

    Example:

    {{
        "questions":[
            {{
                "question":"What is Python?",
                "answer":"Python is a programming language.",
                "difficulty":"Easy"
            }}
        ]
    }}
    """

    return ask_gemini(prompt)