from fastapi import APIRouter
from app.models.report_request import ReportRequest
from app.agents.report_generator import generate_report

router = APIRouter()

@router.post("/generate-report")
def create_report(request: ReportRequest):
    return generate_report(request)