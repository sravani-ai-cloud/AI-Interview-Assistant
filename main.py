from app.database.db import engine
from app.models.user_model import User
from app.database.db import Base
from fastapi import FastAPI

from app.routes.question_routes import router as question_router
from app.routes.interview_routes import router as interview_router
from app.routes.feedback_routes import router as feedback_router
from app.routes.resume_routes import router as resume_router
from app.routes.scorecard_routes import router as scorecard_router
from app.routes.recommendation_routes import router as recommendation_router
from app.routes.report_routes import router as report_router
from app.auth.auth_routes import router as auth_router

app = FastAPI(title="AI Interview Assistant")

Base.metadata.create_all(bind=engine)
app.include_router(question_router)
app.include_router(interview_router)
app.include_router(feedback_router)
app.include_router(resume_router)
app.include_router(scorecard_router)
app.include_router(recommendation_router)
app.include_router(report_router)
app.include_router(auth_router)


@app.get("/")
def home():
    return {
        "message": "AI Interview Assistant"
    }