from app.services.gemini_service import ask_gemini

def analyze_resume(resume, job_description):

    prompt = f"""
    Compare the following resume with the job description.

    Resume:
    {resume}

    Job Description:
    {job_description}

    Return:
    1. Matched Skills
    2. Missing Skills
    3. Improvement Suggestions

    Format as JSON.
    """

    return ask_gemini(prompt)