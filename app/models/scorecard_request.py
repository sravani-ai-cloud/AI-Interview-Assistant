from pydantic import BaseModel

class ScorecardRequest(BaseModel):
    question: str
    answer: str
    feedback: str