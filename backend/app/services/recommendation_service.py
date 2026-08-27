from app.schemas.assessment import AssessmentRequest, AssessmentResponse


SERVICE_SELECTION_RULES = (
    ("Amazon Comprehend", ("sentiment", "customer review")),
    ("Amazon Textract", ("invoice", "extract fields", "tables")),
    ("Amazon Transcribe", ("transcribe", "transcription", "speech-to-text")),
    ("Amazon Rekognition", ("identify objects", "object analysis", "image analysis")),
    ("Amazon Polly", ("text-to-speech", "voice generation", "voice audio")),
    (
        "Amazon SageMaker",
        ("custom machine learning", "custom ml", "model training", "train and deploy"),
    ),
    ("Amazon Bedrock", ("generative ai", "assistant")),
)

SERVICE_METADATA = {
    "Amazon Comprehend": {
        "purpose": (
            "Analyse text for sentiment, entities, key phrases, and other "
            "natural-language insights."
        ),
        "reason_selected": (
            "The business problem requires sentiment analysis of customer text."
        ),
        "implementation_role": (
            "Process text and return language insights to the application."
        ),
    },
    "Amazon Textract": {
        "purpose": (
            "Extract text, forms, fields, and tables from scanned documents."
        ),
        "reason_selected": (
            "The input contains invoices whose fields and tables need extraction."
        ),
        "implementation_role": (
            "Convert business documents into structured data for downstream use."
        ),
    },
    "Amazon Transcribe": {
        "purpose": "Convert speech in audio recordings into text.",
        "reason_selected": (
            "The use case needs spoken content from audio converted into text."
        ),
        "implementation_role": (
            "Produce searchable transcripts for the application workflow."
        ),
    },
    "Amazon Rekognition": {
        "purpose": "Analyse images and video for objects and other visual features.",
        "reason_selected": (
            "The use case requires objects to be detected in image content."
        ),
        "implementation_role": (
            "Provide visual detection results to the application workflow."
        ),
    },
    "Amazon Polly": {
        "purpose": "Convert written text into natural-sounding speech.",
        "reason_selected": (
            "The requested output is text-to-speech narration for users."
        ),
        "implementation_role": (
            "Generate spoken audio from application-provided text."
        ),
    },
    "Amazon SageMaker": {
        "purpose": "Build, train, deploy, and manage custom machine learning models.",
        "reason_selected": (
            "The requirement is to train and deploy a custom model using business data."
        ),
        "implementation_role": (
            "Manage the model lifecycle from experimentation through inference."
        ),
    },
    "Amazon Bedrock": {
        "purpose": (
            "Provide managed access to foundation models for generative AI solutions."
        ),
        "reason_selected": (
            "The use case requires generative AI capabilities for an assistant."
        ),
        "implementation_role": (
            "Return generated responses that the application validates before presenting."
        ),
    },
}


def select_primary_service(
    business_challenge: str,
    input_data_type: str,
) -> str:
    text = f"{business_challenge} {input_data_type}".lower()

    for service_name, keywords in SERVICE_SELECTION_RULES:
        if any(keyword in text for keyword in keywords):
            return service_name

    return "Amazon Bedrock"


def build_mock_recommendation(
    request: AssessmentRequest,
) -> AssessmentResponse:
    primary_service = select_primary_service(
        business_challenge=request.business_challenge,
        input_data_type=request.input_data_type,
    )
    service_metadata = SERVICE_METADATA[primary_service]

    return AssessmentResponse(
        assessment_id="demo-assessment-001",
        status="completed",
        problem_summary=request.business_challenge,
        use_case_category="mock-ai-assessment",
        recommended_services=[
            {
                "service_name": primary_service,
                **service_metadata,
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
