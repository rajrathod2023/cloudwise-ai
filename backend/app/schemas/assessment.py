from typing import Literal

from pydantic import BaseModel, Field


class AssessmentRequest(BaseModel):
    industry: str = Field(min_length=2, max_length=100)
    business_challenge: str = Field(min_length=10, max_length=2000)
    input_data_type: str = Field(min_length=2, max_length=200)
    desired_output: str = Field(min_length=2, max_length=500)
    intended_users: str = Field(min_length=2, max_length=300)

    processing_type: Literal["real-time", "batch", "either"]
    data_sensitivity: Literal["low", "medium", "high"]
    expected_usage: Literal["low", "medium", "high"]
    budget_level: Literal["low", "medium", "high"]

    compliance_requirements: str | None = Field(
        default=None,
        max_length=500,
    )
    additional_context: str | None = Field(
        default=None,
        max_length=2000,
    )


class RecommendedService(BaseModel):
    service_name: str = Field(min_length=2, max_length=100)
    purpose: str = Field(min_length=5, max_length=500)
    reason_selected: str = Field(min_length=5, max_length=1000)
    implementation_role: str = Field(min_length=2, max_length=300)


class ArchitectureComponent(BaseModel):
    component_name: str = Field(min_length=2, max_length=100)
    aws_service: str = Field(min_length=2, max_length=100)
    responsibility: str = Field(min_length=5, max_length=500)


class ImplementationPhase(BaseModel):
    phase_number: int = Field(ge=1, le=10)
    title: str = Field(min_length=2, max_length=100)
    description: str = Field(min_length=5, max_length=1000)


class ResponsibleAI(BaseModel):
    risks: list[str]
    mitigations: list[str]
    human_review_required: bool
    explanation: str = Field(min_length=10, max_length=1000)


class SecurityAssessment(BaseModel):
    iam_controls: list[str]
    encryption_controls: list[str]
    logging_controls: list[str]
    data_protection_notes: str = Field(
        min_length=10,
        max_length=1000,
    )


class PrivacyComplianceAssessment(BaseModel):
    privacy_considerations: list[str]
    compliance_considerations: list[str]
    data_retention_notes: str = Field(
        min_length=10,
        max_length=1000,
    )


class AssessmentResponse(BaseModel):
    assessment_id: str
    status: Literal["completed"]

    problem_summary: str = Field(
        min_length=10,
        max_length=2000,
    )
    use_case_category: str = Field(
        min_length=2,
        max_length=200,
    )

    recommended_services: list[RecommendedService]
    architecture: list[ArchitectureComponent]
    implementation_phases: list[ImplementationPhase]

    responsible_ai: ResponsibleAI
    security: SecurityAssessment
    privacy_and_compliance: PrivacyComplianceAssessment

    limitations: list[str]
    alternatives_considered: list[str]

    complexity: Literal["low", "medium", "high"]
    cost_level: Literal["low", "medium", "high"]

    disclaimer: str = Field(
        min_length=10,
        max_length=1000,
    )