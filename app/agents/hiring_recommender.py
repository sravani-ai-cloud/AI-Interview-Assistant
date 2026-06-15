from app.services.gemini_service import ask_gemini

def generate_recommendation(scorecard, resume_analysis):

    prompt = f"""
    You are a senior hiring manager.

    Scorecard:
    {scorecard}

    Resume Analysis:
    {resume_analysis}

    Based on the above information provide:

    1. Hiring Decision
    2. Strengths
    3. Concerns
    4. Final Recommendation

    Return JSON format.
    """

    return ask_gemini(prompt)