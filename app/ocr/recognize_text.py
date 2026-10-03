import pytesseract


def recognize_text(img):
    text = pytesseract.image_to_string(img, lang='rus+eng')
    return text