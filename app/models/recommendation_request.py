from pydantic import BaseModel

class RecommendationRequest(BaseModel):
    scorecard: str
    resume_analysis: str