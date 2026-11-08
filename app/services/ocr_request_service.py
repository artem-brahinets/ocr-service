from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import OCRRequest


def save_ocr_request(db: Session, image_hash: str, recognized_text: str):
    request = OCRRequest(
        image_hash=image_hash,
        recognized_text=recognized_text
    )

    db.add(request)
    db.commit()

    return request


def get_ocr_request(db: Session, image_hash: str):
    statement = select(OCRRequest).where(
        OCRRequest.image_hash == image_hash
    )

    result = db.scalar(statement)

    return result
