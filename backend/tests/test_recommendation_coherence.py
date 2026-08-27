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
        "component_term",
        "responsibility_term",
        "phase_title_term",
        "phase_description_term",
        "limitation_term",
        "alternative_term",
    ),
    [
        (
            "Extract fields and tables from supplier invoices",
            "Scanned invoices",
            "Amazon Textract",
            "document extraction",
            "fields and tables",
            "Textract integration",
            "documents",
            "document quality",
            "manual extraction",
        ),
        (
            "Transcribe customer support calls into text",
            "Audio recordings",
            "Amazon Transcribe",
            "transcription",
            "audio into text",
            "Transcribe integration",
            "audio",
            "audio quality",
            "manual transcription",
        ),
        (
            "Train and deploy a custom machine learning model",
            "Training dataset",
            "Amazon SageMaker",
            "custom ML",
            "model training",
            "SageMaker model workflow",
            "training",
            "training data",
            "managed prebuilt AI service",
        ),
        (
            "Build a generative AI assistant for employees",
            "Internal business documents",
            "Amazon Bedrock",
            "generative AI",
            "foundation models",
            "Bedrock integration",
            "foundation model",
            "hallucinate",
            "specialised AWS AI service",
        ),
    ],
)
def test_recommendation_is_coherent_with_selected_service(
    business_challenge: str,
    input_data_type: str,
    expected_service: str,
    component_term: str,
    responsibility_term: str,
    phase_title_term: str,
    phase_description_term: str,
    limitation_term: str,
    alternative_term: str,
):
    recommendation = build_mock_recommendation(
        build_request(business_challenge, input_data_type)
    )
    ai_component = next(
        component
        for component in recommendation.architecture
        if component.aws_service == expected_service
    )
    integration_phase = recommendation.implementation_phases[1]

    assert component_term.lower() in ai_component.component_name.lower()
    assert responsibility_term.lower() in ai_component.responsibility.lower()
    assert phase_title_term.lower() in integration_phase.title.lower()
    assert phase_description_term.lower() in integration_phase.description.lower()
    assert any(
        limitation_term.lower() in limitation.lower()
        for limitation in recommendation.limitations
    )
    assert any(
        alternative_term.lower() in alternative.lower()
        for alternative in recommendation.alternatives_considered
    )
