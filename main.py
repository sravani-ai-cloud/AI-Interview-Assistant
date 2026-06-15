from fastapi import FastAPI

from app.routes.question_routes import router as question_router
from app.routes.interview_routes import router as interview_router
from app.routes.feedback_routes import router as feedback_router

app = FastAPI(title="AI Interview Assistant")

app.include_router(question_router)
app.include_router(interview_router)
app.include_router(feedback_router)


@app.get("/")
def home():
    return {
        "message": "AI Interview Assistant"
    }