from app.ocr.preprocessing import preprocess
from app.ocr.recognize_text import recognize_text


def ocr_img(image: bytes) -> str:
    preprocessed_img = preprocess(image)
    text = recognize_text(preprocessed_img)

    return text