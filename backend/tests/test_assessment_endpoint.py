from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_assessment():
    payload = {
        "industry": "Retail",
        "business_challenge": (
            "Analyse customer feedback and recommend an AWS AI solution."
        ),
        "input_data_type": "Customer review text",
        "desired_output": "AWS AI architecture recommendation",
        "intended_users": "Business and technical teams",
        "processing_type": "batch",
        "data_sensitivity": "medium",
        "expected_usage": "medium",
        "budget_level": "low",
        "compliance_requirements": (
            "Customer information must be handled carefully."
        ),
        "additional_context": (
            "Recommendations require human review before implementation."
        ),
    }

    response = client.post("/api/v1/assessments", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "completed"
    assert data["problem_summary"] == payload["business_challenge"]
    assert data["assessment_id"] == "cloudwise-assessment-v1"
    assert data["use_case_category"] == "aws-ai-solution-assessment"
    assert data["recommended_services"][0]["service_name"] == "Amazon Comprehend"
    response_text = response.text.lower()
    assert "mock-ai-assessment" not in response_text
    assert "mocked recommendations" not in response_text
    assert "demo-assessment" not in response_text


def test_create_assessment_rejects_invalid_processing_type():
    payload = {
        "industry": "Retail",
        "business_challenge": (
            "Analyse customer feedback and recommend an AWS AI solution."
        ),
        "input_data_type": "Customer review text",
        "desired_output": "AWS AI architecture recommendation",
        "intended_users": "Business and technical teams",
        "processing_type": "instant",
        "data_sensitivity": "medium",
        "expected_usage": "medium",
        "budget_level": "low",
    }

    response = client.post("/api/v1/assessments", json=payload)

    assert response.status_code == 422


def test_create_assessment_selects_textract_for_invoice_extraction():
    payload = {
        "industry": "Finance",
        "business_challenge": "Extract fields and tables from supplier invoices.",
        "input_data_type": "Scanned invoices",
        "desired_output": "Structured invoice data",
        "intended_users": "Accounts payable team",
        "processing_type": "batch",
        "data_sensitivity": "medium",
        "expected_usage": "medium",
        "budget_level": "medium",
        "compliance_requirements": (
            "Financial documents must be handled securely."
        ),
        "additional_context": (
            "The extracted data will be reviewed before downstream processing."
        ),
    }

    response = client.post("/api/v1/assessments", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["recommended_services"][0]["service_name"] == "Amazon Textract"
