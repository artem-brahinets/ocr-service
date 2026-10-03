import pytest
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


@pytest.fixture
def test_image():
    with open("tests/test_images/img_2.png", "rb") as image:
        return image.read()


def test_ocr_endpoint(test_image):
    response = client.post(
        "/ocr",
        files={"image": ("img_2.png", test_image, "image/png")}
    )

    assert response.status_code == 200

    data = response.json()

    assert "text_from_img" in data
    assert "Hello World!" in data["text_from_img"]