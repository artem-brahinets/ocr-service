import pytest
from app.services.ocr_service import ocr_img


@pytest.fixture
def test_image():
    with open("tests/test_images/img_2.png", "rb") as image:
        return image.read()


def test_ocr(test_image):
    result = ocr_img(test_image)

    assert "Hello World!" in result