from app.schemas.assessment import AssessmentRequest, AssessmentResponse


def select_primary_service(
    business_challenge: str,
    input_data_type: str,
) -> str:
    text = f"{business_challenge} {input_data_type}".lower()

    if "sentiment" in text or "customer review" in text:
        return "Amazon Comprehend"

    if "invoice" in text or "extract fields" in text or "tables" in text:
        return "Amazon Textract"

    if "generative ai" in text or "assistant" in text:
        return "Amazon Bedrock"

    return "Amazon Bedrock"


def build_mock_recommendation(
    request: AssessmentRequest,
) -> AssessmentResponse:
    primary_service = select_primary_service(
        business_challenge=request.business_challenge,
        input_data_type=request.input_data_type,
    )

    return AssessmentResponse(
        assessment_id="demo-assessment-001",
        status="completed",
        problem_summary=request.business_challenge,
        use_case_category="mock-ai-assessment",
        recommended_services=[
            {
                "service_name": primary_service,
                "purpose": "Provide the primary AI capability for the use case.",
                "reason_selected": (
                    "Selected based on the business challenge and input data type."
                ),
                "implementation_role": "Primary AI service",
            }
        ],
        architecture=[
            {
                "component_name": "API Layer",
                "aws_service": "Amazon API Gateway",
                "responsibility": (
                    "Receive assessment requests and route them to the backend."
                ),
            },
            {
                "component_name": "Backend Processing",
                "aws_service": "AWS Lambda",
                "responsibility": (
                    "Run the FastAPI backend and process validated "
                    "assessment requests."
                ),
            },
            {
                "component_name": "AI Recommendation",
                "aws_service": primary_service,
                "responsibility": (
                    "Provide the primary AI capability selected for the "
                    "business use case."
                ),
            },
        ],
        implementation_phases=[
            {
                "phase_number": 1,
                "title": "Proof of Concept",
                "description": (
                    "Validate the business use case with mocked recommendations "
                    "before connecting real AWS AI services."
                ),
            },
            {
                "phase_number": 2,
                "title": "AWS AI Integration",
                "description": (
                    "Connect the selected AWS AI service and validate "
                    "structured application responses."
                ),
            },
        ],
        responsible_ai={
            "risks": [
                "AI recommendations may contain inaccurate or incomplete information.",
                "Generated recommendations may reflect model or data bias.",
            ],
            "mitigations": [
                "Require human review before implementation.",
                "Validate structured output before returning it to the user.",
                "Use clear disclaimers and responsible-AI guidance.",
            ],
            "human_review_required": True,
            "explanation": (
                "CloudWise AI provides advisory recommendations only. "
                "A qualified person should review the proposed solution "
                "before implementation."
            ),
        },
        security={
            "iam_controls": [
                "Use least-privilege IAM permissions.",
                "Restrict access to required AWS services only.",
            ],
            "encryption_controls": [
                "Use encryption in transit.",
                "Use encryption at rest for stored assessment data.",
            ],
            "logging_controls": [
                "Record application logs in Amazon CloudWatch.",
                "Use AWS CloudTrail for AWS API auditing.",
            ],
            "data_protection_notes": (
                "Do not store AWS credentials, secrets, or unnecessary "
                "sensitive data in application source code or logs."
            ),
        },
        privacy_and_compliance={
            "privacy_considerations": [
                "Collect only the minimum data required for the assessment.",
                "Avoid including unnecessary personal or sensitive information "
                "in AI requests.",
            ],
            "compliance_considerations": [
                "Review applicable industry and organisational compliance "
                "requirements.",
                "Confirm that selected AWS services and data locations meet "
                "business obligations.",
            ],
            "data_retention_notes": (
                "Define how long assessment data should be retained and remove "
                "it when it is no longer required."
            ),
        },
        limitations=[
            "The recommendation currently uses rule-based service selection.",
            "The proposed architecture must be validated against current AWS "
            "service capabilities.",
            "Cost estimates are indicative and depend on actual usage patterns.",
        ],
        alternatives_considered=[
            "Use another specialised AWS AI service when it better matches "
            "the business requirement.",
            "Use a simpler non-AI workflow when AI does not provide sufficient "
            "business value.",
        ],
        complexity="medium",
        cost_level="low",
        disclaimer=(
            "This is a development recommendation and must be reviewed "
            "before implementation."
        ),
    )