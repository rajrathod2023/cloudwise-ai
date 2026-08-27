from app.services.recommendation_service import select_primary_service


def test_selects_comprehend_for_sentiment_analysis():
    service = select_primary_service(
        business_challenge="Analyse customer sentiment from product reviews",
        input_data_type="Customer review text",
    )

    assert service == "Amazon Comprehend"


def test_selects_textract_for_invoice_extraction():
    service = select_primary_service(
        business_challenge="Extract fields and tables from invoices",
        input_data_type="Scanned invoices",
    )

    assert service == "Amazon Textract"


def test_selects_bedrock_for_generative_ai_assistant():
    service = select_primary_service(
        business_challenge="Build a generative AI assistant for employees",
        input_data_type="Internal business documents",
    )

    assert service == "Amazon Bedrock"


def test_selects_transcribe_for_audio_transcription():
    service = select_primary_service(
        business_challenge="Transcribe customer support calls into text",
        input_data_type="Audio recordings",
    )

    assert service == "Amazon Transcribe"


def test_selects_rekognition_for_image_object_analysis():
    service = select_primary_service(
        business_challenge="Identify objects in warehouse images",
        input_data_type="Images",
    )

    assert service == "Amazon Rekognition"


def test_selects_polly_for_text_to_speech_voice_generation():
    service = select_primary_service(
        business_challenge="Generate natural voice audio from written content",
        input_data_type="Text",
    )

    assert service == "Amazon Polly"


def test_selects_sagemaker_for_custom_ml_model_training_and_deployment():
    service = select_primary_service(
        business_challenge="Train and deploy a custom machine learning model",
        input_data_type="Training dataset",
    )

    assert service == "Amazon SageMaker"
