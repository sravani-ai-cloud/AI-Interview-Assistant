from fastapi import APIRouter
from app.models.scorecard_request import ScorecardRequest
from app.agents.scorecard_generator import generate_scorecard

router = APIRouter()

@router.post("/generate-scorecard")
def scorecard(request: ScorecardRequest):

    result = generate_scorecard(
        request.question,
        request.answer,
        request.feedback
    )

    return {"result": result}