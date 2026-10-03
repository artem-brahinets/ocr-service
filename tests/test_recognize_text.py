from app.ocr.recognize_text import recognize_text
from app.ocr.preprocessing import preprocess
import pytest


@pytest.fixture
def test_image():
    with open('tests/test_images/img.png', 'rb') as test_image:
        return test_image.read()

def test_recognize_text(test_image):
    image = preprocess(test_image)
    result = recognize_text(image)

    assert isinstance(result, str)
    assert result.strip()