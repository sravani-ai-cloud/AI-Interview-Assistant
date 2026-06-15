from fastapi import APIRouter

from app.models.question_request import QuestionRequest
from app.agents.question_generator import generate_questions

router = APIRouter()


@router.post("/generate-questions")
def get_questions(request: QuestionRequest):

    questions = generate_questions(
        request.technology,
        request.level
    )

    return {
        "questions": questions
    }