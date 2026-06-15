from fastapi import APIRouter

from app.models.question_request import QuestionRequest
from app.agents.interview_generator import generate_interview

router = APIRouter()


@router.post("/generate-interview")
def interview(request: QuestionRequest):

    result = generate_interview(
        request.technology,
        request.level
    )

    return {
        "result": result
    }