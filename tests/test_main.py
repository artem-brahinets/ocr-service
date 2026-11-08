import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def test_image():
    with open("tests/test_images/img_2.png", "rb") as image:
        return image.read()


def test_ocr_endpoint(client, test_image):
    response = client.post(
        "/ocr",
        files={"image": ("img_2.png", test_image, "image/png")}
    )

    assert response.status_code == 200

    data = response.json()

    assert "text_from_img" in data
    assert "Hello World!" in data["text_from_img"]