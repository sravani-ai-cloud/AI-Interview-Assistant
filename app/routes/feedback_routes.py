from fastapi import APIRouter

from app.models.feedback_request import FeedbackRequest
from app.agents.feedback_agent import evaluate_answer

router = APIRouter()


@router.post("/evaluate-answer")
def feedback(request: FeedbackRequest):

    result = evaluate_answer(
        request.question,
        request.answer
    )

    return {
        "result": result
    }