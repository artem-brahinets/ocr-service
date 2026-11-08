from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.db.database import get_db
from app.db.models import Base
from app.main import app


@pytest.fixture
def test_db():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    TestingSessionLocal = sessionmaker(bind=engine)

    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)
        engine.dispose()


@pytest.fixture
def client(test_db):
    def override_get_db():
        try:
            yield test_db
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


def test_ocr_result_is_cached(client):
    image_bytes = b"fake image content"

    with patch(
        "app.main.ocr_service.ocr_img",
        return_value="Test recognized text",
    ) as mock_ocr:

        response1 = client.post(
            "/ocr",
            files={"image": ("test.png", image_bytes, "image/png")},
        )

        assert response1.status_code == 200
        assert response1.json() == {
            "text_from_img": "Test recognized text"
        }

        response2 = client.post(
            "/ocr",
            files={"image": ("test.png", image_bytes, "image/png")},
        )

        assert response2.status_code == 200
        assert response2.json() == {
            "text_from_img": "Test recognized text"
        }

        mock_ocr.assert_called_once()