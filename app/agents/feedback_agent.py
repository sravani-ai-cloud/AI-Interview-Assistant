from app.services.gemini_service import ask_gemini


def evaluate_answer(question, answer):

    prompt = f"""
    You are a senior technical interviewer.

    Evaluate the candidate's answer.

    Question:
    {question}

    Candidate Answer:
    {answer}

    Give:

    1. Score out of 10
    2. Feedback
    3. Improvement Suggestions

    Return response in JSON format.
    """

    return ask_gemini(prompt)