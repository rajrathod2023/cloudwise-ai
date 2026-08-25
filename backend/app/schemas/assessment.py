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