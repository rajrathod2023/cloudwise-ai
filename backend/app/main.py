from fastapi import FastAPI

from app.schemas.assessment import AssessmentRequest, AssessmentResponse


app = FastAPI(
    title="CloudWise AI API",
    description="Backend API for the CloudWise AI AWS Solution Advisor.",
    version="0.1.0",
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
    return {
        "assessment_id": "demo-assessment-001",
        "status": "completed",
        "problem_summary": request.business_challenge,
        "use_case_category": "mock-ai-assessment",
        "recommended_services": [
            {
                "service_name": "Amazon Bedrock",
                "purpose": "Generate a structured AWS AI recommendation.",
                "reason_selected": (
                    "Used as the planned generative AI layer for CloudWise AI."
                ),
                "implementation_role": "AI recommendation engine",
            }
        ],
        "complexity": "medium",
        "cost_level": "low",
        "disclaimer": (
            "This is a mocked recommendation for development and testing. "
            "It must be reviewed before implementation."
        ),
    }