from app.ocr.preprocessing import preprocess
import pytest
import numpy as np


@pytest.fixture
def invalid_image():
    return b"this is not an image"


@pytest.fixture
def test_image():
    with open("tests/test_images/img.png", "rb") as image:
        return image.read()


def test_invalid_preprocessing(invalid_image):
    with pytest.raises(ValueError, match="Failed to decode image"):
        preprocess(invalid_image)


def test_preprocessing(test_image):
    result = preprocess(test_image)

    assert isinstance(result, np.ndarray)

