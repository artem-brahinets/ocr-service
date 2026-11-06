import hashlib

from app.ocr.preprocessing import preprocess
from app.ocr.recognize_text import recognize_text


def ocr_img(image: bytes) -> str:
    preprocessed_img = preprocess(image)
    text = recognize_text(preprocessed_img)

    return text


def hash_image(image: bytes) -> str:
    image_hash = hashlib.sha256(image).hexdigest()
    return image_hash