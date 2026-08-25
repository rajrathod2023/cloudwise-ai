import pytest
from pydantic import ValidationError

from app.schemas.assessment import AssessmentRequest


def test_valid_assessment_request():
    request = AssessmentRequest(
        industry="Healthcare",
        business_challenge="Summarise incoming referral documents for clinical review.",
        input_data_type="Scanned documents and text",
        desired_output="Structured summary",
        intended_users="Clinical administration staff",
        processing_type="batch",
        data_sensitivity="high",
        expected_usage="medium",
        budget_level="medium",
        compliance_requirements="Sensitive health information",
        additional_context="Human review is required before use.",
    )

    assert request.industry == "Healthcare"
    assert request.processing_type == "batch"


def test_invalid_processing_type():
    with pytest.raises(ValidationError):
        AssessmentRequest(
            industry="Healthcare",
            business_challenge="Summarise incoming referral documents for clinical review.",
            input_data_type="Scanned documents",
            desired_output="Structured summary",
            intended_users="Clinical staff",
            processing_type="very-fast",
            data_sensitivity="high",
            expected_usage="medium",
            budget_level="medium",
        )