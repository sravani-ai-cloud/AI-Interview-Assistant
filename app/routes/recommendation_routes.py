from fastapi import APIRouter
from app.models.recommendation_request import RecommendationRequest
from app.agents.hiring_recommender import generate_recommendation

router = APIRouter()

@router.post("/generate-recommendation")
def recommendation(request: RecommendationRequest):

    result = generate_recommendation(
        request.scorecard,
        request.resume_analysis
    )

    return {"result": result}