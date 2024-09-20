import os
import pytest
from app.services import extract_text_from_image


@pytest.fixture(scope="module")
def image_path():
    path = 'tests/uploads/ocr_test.jpg'
    assert os.path.exists(path), f"Image not found: {path}"
    return path


@pytest.mark.asyncio
async def test_textract_endpoint_connection() -> None:
    # given
    from lib.aws_boto3 import textract
    # when
    response = textract.list_adapters()
    # then
    assert response['ResponseMetadata']['HTTPStatusCode'] == 200


@pytest.mark.asyncio
async def test_ocr_extraction(image_path) -> None:
   # given image_path
    # when
    results = await extract_text_from_image(image_path)
    # then
    for item in results:
        assert 'text' in item and isinstance(item["text"], str)
        assert 'confidence' in item and isinstance(item["confidence"], float)
