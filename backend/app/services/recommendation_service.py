from typing import Literal

from app.schemas.assessment import AssessmentRequest, AssessmentResponse


PlanningLevel = Literal["low", "medium", "high"]


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
        "architecture_component_name": "Natural Language Analysis",
        "architecture_responsibility": (
            "Analyse text for sentiment, entities, and key phrases."
        ),
        "integration_phase_title": "Amazon Comprehend Integration",
        "integration_phase_description": (
            "Connect Amazon Comprehend and validate text-analysis results."
        ),
        "limitations": [
            "Language support and domain-specific wording can affect analysis quality."
        ],
        "alternatives": [
            "Consider deterministic text processing when AI analysis is unnecessary."
        ],
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
        "architecture_component_name": "Document Extraction",
        "architecture_responsibility": (
            "Extract text, forms, fields and tables from business documents."
        ),
        "integration_phase_title": "Amazon Textract Integration",
        "integration_phase_description": (
            "Connect Amazon Textract and validate extraction against sample documents."
        ),
        "limitations": [
            "Document quality and layout complexity can affect extraction accuracy."
        ],
        "alternatives": [
            "Consider manual extraction or deterministic document templates for "
            "small, predictable workloads."
        ],
    },
    "Amazon Transcribe": {
        "purpose": "Convert speech in audio recordings into text.",
        "reason_selected": (
            "The use case needs spoken content from audio converted into text."
        ),
        "implementation_role": (
            "Produce searchable transcripts for the application workflow."
        ),
        "architecture_component_name": "Audio Transcription",
        "architecture_responsibility": (
            "Convert spoken audio into text for downstream processing."
        ),
        "integration_phase_title": "Amazon Transcribe Integration",
        "integration_phase_description": (
            "Connect Amazon Transcribe and validate transcripts using representative audio."
        ),
        "limitations": [
            "Audio quality, background noise, and speaker accents can affect accuracy."
        ],
        "alternatives": [
            "Consider manual transcription for low-volume or highly sensitive recordings."
        ],
    },
    "Amazon Rekognition": {
        "purpose": "Analyse images and video for objects and other visual features.",
        "reason_selected": (
            "The use case requires objects to be detected in image content."
        ),
        "implementation_role": (
            "Provide visual detection results to the application workflow."
        ),
        "architecture_component_name": "Visual Analysis",
        "architecture_responsibility": (
            "Analyse images and video for objects and other visual features."
        ),
        "integration_phase_title": "Amazon Rekognition Integration",
        "integration_phase_description": (
            "Connect Amazon Rekognition and validate detections using representative media."
        ),
        "limitations": [
            "Image quality, viewing angle, and visual context can affect detection results."
        ],
        "alternatives": [
            "Consider human visual review when context or accuracy requirements exceed "
            "automated detection capabilities."
        ],
    },
    "Amazon Polly": {
        "purpose": "Convert written text into natural-sounding speech.",
        "reason_selected": (
            "The requested output is text-to-speech narration for users."
        ),
        "implementation_role": (
            "Generate spoken audio from application-provided text."
        ),
        "architecture_component_name": "Speech Synthesis",
        "architecture_responsibility": (
            "Convert application text into natural-sounding speech."
        ),
        "integration_phase_title": "Amazon Polly Integration",
        "integration_phase_description": (
            "Connect Amazon Polly and validate voice output with representative text."
        ),
        "limitations": [
            "Pronunciation, voice choice, and language availability can affect output."
        ],
        "alternatives": [
            "Consider recorded human narration when a highly specific voice is required."
        ],
    },
    "Amazon SageMaker": {
        "purpose": "Build, train, deploy, and manage custom machine learning models.",
        "reason_selected": (
            "The requirement is to train and deploy a custom model using business data."
        ),
        "implementation_role": (
            "Manage the model lifecycle from experimentation through inference."
        ),
        "architecture_component_name": "Custom ML Workflow",
        "architecture_responsibility": (
            "Support model training, deployment, and inference for the custom use case."
        ),
        "integration_phase_title": "Amazon SageMaker Model Workflow",
        "integration_phase_description": (
            "Prepare training data, train and evaluate the model, then validate deployment."
        ),
        "limitations": [
            "Custom ML requires suitable training data and ongoing model lifecycle management."
        ],
        "alternatives": [
            "Consider a managed prebuilt AI service before building a custom model."
        ],
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
        "architecture_component_name": "Generative AI",
        "architecture_responsibility": (
            "Use foundation models to generate responses for the application."
        ),
        "integration_phase_title": "Amazon Bedrock Integration",
        "integration_phase_description": (
            "Connect a suitable foundation model and validate structured responses."
        ),
        "limitations": [
            "Generative AI can hallucinate or produce inaccurate and biased output."
        ],
        "alternatives": [
            "Consider a specialised AWS AI service when generative AI is unnecessary."
        ],
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


def estimate_complexity(
    processing_type: str,
    data_sensitivity: str,
    expected_usage: str,
    selected_service: str,
) -> PlanningLevel:
    score = 0

    if processing_type == "real-time":
        score += 1

    score += {"low": 0, "medium": 1, "high": 2}[data_sensitivity]
    score += {"low": 0, "medium": 1, "high": 2}[expected_usage]

    if selected_service == "Amazon SageMaker":
        score += 2

    if score <= 1:
        return "low"
    if score <= 3:
        return "medium"
    return "high"


def estimate_cost_level(
    expected_usage: str,
    processing_type: str,
    selected_service: str,
) -> PlanningLevel:
    score = {"low": 0, "medium": 1, "high": 3}[expected_usage]

    if processing_type == "real-time":
        score += 1
    if selected_service == "Amazon SageMaker":
        score += 1

    if score == 0:
        return "low"
    if score <= 2:
        return "medium"
    return "high"


def build_mock_recommendation(
    request: AssessmentRequest,
) -> AssessmentResponse:
    primary_service = select_primary_service(
        business_challenge=request.business_challenge,
        input_data_type=request.input_data_type,
    )
    service_metadata = SERVICE_METADATA[primary_service]
    complexity = estimate_complexity(
        processing_type=request.processing_type,
        data_sensitivity=request.data_sensitivity,
        expected_usage=request.expected_usage,
        selected_service=primary_service,
    )
    cost_level = estimate_cost_level(
        expected_usage=request.expected_usage,
        processing_type=request.processing_type,
        selected_service=primary_service,
    )

    return AssessmentResponse(
        assessment_id="demo-assessment-001",
        status="completed",
        problem_summary=request.business_challenge,
        use_case_category="mock-ai-assessment",
        recommended_services=[
            {
                "service_name": primary_service,
                "purpose": service_metadata["purpose"],
                "reason_selected": service_metadata["reason_selected"],
                "implementation_role": service_metadata["implementation_role"],
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
                "component_name": service_metadata["architecture_component_name"],
                "aws_service": primary_service,
                "responsibility": service_metadata["architecture_responsibility"],
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
                "title": service_metadata["integration_phase_title"],
                "description": service_metadata["integration_phase_description"],
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
            *service_metadata["limitations"],
        ],
        alternatives_considered=[
            *service_metadata["alternatives"],
            "Use a simpler non-AI workflow when AI does not provide sufficient "
            "business value.",
        ],
        complexity=complexity,
        cost_level=cost_level,
        disclaimer=(
            "This is a development recommendation and must be reviewed "
            "before implementation."
        ),
    )
