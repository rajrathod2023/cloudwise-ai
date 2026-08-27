import pytest

from app.schemas.assessment import AssessmentRequest
from app.services.recommendation_service import build_mock_recommendation


def build_request(
    business_challenge: str,
    input_data_type: str,
) -> AssessmentRequest:
    return AssessmentRequest(
        industry="Technology",
        business_challenge=business_challenge,
        input_data_type=input_data_type,
        desired_output="A suitable AWS AI solution",
        intended_users="Business and technical teams",
        processing_type="batch",
        data_sensitivity="medium",
        expected_usage="medium",
        budget_level="medium",
    )


@pytest.mark.parametrize(
    (
        "business_challenge",
        "input_data_type",
        "expected_service",
        "purpose_term",
        "reason_term",
        "role_term",
    ),
    [
        (
            "Analyse customer sentiment from product reviews",
            "Customer review text",
            "Amazon Comprehend",
            "text",
            "sentiment",
            "insights",
        ),
        (
            "Extract fields and tables from supplier invoices",
            "Scanned invoices",
            "Amazon Textract",
            "documents",
            "form fields",
            "structured data",
        ),
        (
            "Transcribe customer support calls into text",
            "Audio recordings",
            "Amazon Transcribe",
            "speech",
            "audio",
            "transcripts",
        ),
        (
            "Identify objects in warehouse images",
            "Images",
            "Amazon Rekognition",
            "images",
            "objects",
            "visual",
        ),
        (
            "Create text-to-speech narration for training content",
            "Written text",
            "Amazon Polly",
            "speech",
            "text-to-speech",
            "audio",
        ),
        (
            "Train and deploy a custom machine learning model",
            "Training dataset",
            "Amazon SageMaker",
            "custom machine learning models",
            "built and trained",
            "model lifecycle",
        ),
        (
            "Build a generative AI assistant for employees",
            "Internal business documents",
            "Amazon Bedrock",
            "foundation models",
            "generative AI",
            "generated responses",
        ),
    ],
)
def test_recommendation_includes_service_specific_metadata(
    business_challenge: str,
    input_data_type: str,
    expected_service: str,
    purpose_term: str,
    reason_term: str,
    role_term: str,
):
    recommendation = build_mock_recommendation(
        build_request(business_challenge, input_data_type)
    )
    service = recommendation.recommended_services[0]

    assert service.service_name == expected_service
    assert purpose_term.lower() in service.purpose.lower()
    assert reason_term.lower() in service.reason_selected.lower()
    assert role_term.lower() in service.implementation_role.lower()
