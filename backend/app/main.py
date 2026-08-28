from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas.assessment import AssessmentRequest, AssessmentResponse
from app.services.recommendation_service import build_recommendation


app = FastAPI(
    title="CloudWise AI API",
    description="Backend API for the CloudWise AI AWS Solution Advisor.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "cloudwise-ai-backend",
        "version": "0.1.0",
    }


@app.post(
    "/api/v1/assessments",
    response_model=AssessmentResponse,
)
def create_assessment(request: AssessmentRequest):
    return build_recommendation(request)
