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