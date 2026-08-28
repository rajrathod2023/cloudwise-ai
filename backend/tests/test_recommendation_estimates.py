from app.schemas.assessment import AssessmentRequest
from app.services.recommendation_service import build_recommendation


def build_request(
    *,
    business_challenge: str,
    input_data_type: str,
    processing_type: str,
    data_sensitivity: str,
    expected_usage: str,
    budget_level: str = "medium",
) -> AssessmentRequest:
    return AssessmentRequest(
        industry="Technology",
        business_challenge=business_challenge,
        input_data_type=input_data_type,
        desired_output="A suitable AWS AI solution",
        intended_users="Business and technical teams",
        processing_type=processing_type,
        data_sensitivity=data_sensitivity,
        expected_usage=expected_usage,
        budget_level=budget_level,
    )


def test_estimates_low_complexity_and_cost_for_simple_batch_workload():
    request = build_request(
        business_challenge="Extract fields from supplier invoices",
        input_data_type="Scanned invoices",
        processing_type="batch",
        data_sensitivity="low",
        expected_usage="low",
    )

    recommendation = build_recommendation(request)

    assert recommendation.complexity == "low"
    assert recommendation.cost_level == "low"


def test_estimates_medium_complexity_and_cost_for_moderate_realtime_workload():
    request = build_request(
        business_challenge="Build a generative AI assistant for employees",
        input_data_type="Internal business documents",
        processing_type="real-time",
        data_sensitivity="medium",
        expected_usage="medium",
    )

    recommendation = build_recommendation(request)

    assert recommendation.complexity == "medium"
    assert recommendation.cost_level == "medium"


def test_estimates_high_complexity_and_cost_for_demanding_custom_ml_workload():
    request = build_request(
        business_challenge="Train and deploy a custom machine learning model",
        input_data_type="Sensitive training dataset",
        processing_type="real-time",
        data_sensitivity="high",
        expected_usage="high",
    )

    recommendation = build_recommendation(request)

    assert recommendation.complexity == "high"
    assert recommendation.cost_level == "high"


def test_budget_constraint_does_not_determine_estimated_cost_level():
    request_values = {
        "business_challenge": "Build a generative AI assistant for employees",
        "input_data_type": "Internal business documents",
        "processing_type": "real-time",
        "data_sensitivity": "medium",
        "expected_usage": "medium",
    }

    low_budget_recommendation = build_recommendation(
        build_request(**request_values, budget_level="low")
    )
    high_budget_recommendation = build_recommendation(
        build_request(**request_values, budget_level="high")
    )

    assert low_budget_recommendation.cost_level == "medium"
    assert high_budget_recommendation.cost_level == "medium"
