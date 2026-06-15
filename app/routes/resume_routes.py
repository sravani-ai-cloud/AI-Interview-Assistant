from fastapi import APIRouter
from app.models.resume_request import ResumeRequest
from app.agents.resume_analyzer import analyze_resume

router = APIRouter()

@router.post("/analyze-resume")
def analyze(data: ResumeRequest):

    result = analyze_resume(
        data.resume,
        data.job_description
    )

    return {"result": result}