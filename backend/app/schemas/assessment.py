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

    compliance_requirements: str | None = Field(default=None, max_length=500)
    additional_context: str | None = Field(default=None, max_length=2000)


class RecommendedService(BaseModel):
    service_name: str = Field(min_length=2, max_length=100)
    purpose: str = Field(min_length=5, max_length=500)
    reason_selected: str = Field(min_length=5, max_length=1000)
    implementation_role: str = Field(min_length=2, max_length=300)


class AssessmentResponse(BaseModel):
    assessment_id: str
    status: Literal["completed"]
    problem_summary: str = Field(min_length=10, max_length=2000)
    use_case_category: str = Field(min_length=2, max_length=200)
    recommended_services: list[RecommendedService]
    complexity: Literal["low", "medium", "high"]
    cost_level: Literal["low", "medium", "high"]
    disclaimer: str = Field(min_length=10, max_length=1000)