from pydantic import BaseModel

class ReportRequest(BaseModel):
    candidate_name: str
    question: str
    answer: str
    score: int
    recommendation: str