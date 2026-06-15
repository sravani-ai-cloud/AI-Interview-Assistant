from app.services.gemini_service import ask_gemini

def generate_scorecard(question, answer, feedback):

    prompt = f"""
    You are a Senior Technical Interviewer.

    Evaluate the candidate using:

    Question:
    {question}

    Candidate Answer:
    {answer}

    Previous Feedback:
    {feedback}

    Return JSON format:

    {{
      "overall_score": 8,
      "technical_knowledge": 8,
      "communication": 7,
      "problem_solving": 7,
      "recommendation": "Hire",
      "summary": "Candidate demonstrates good technical understanding."
    }}
    """

    return ask_gemini(prompt)