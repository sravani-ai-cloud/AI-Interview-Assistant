from pydantic import BaseModel


class QuestionRequest(BaseModel):
    technology: str
    level: str