import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  


def perform_ocr(image_path):
    text = pytesseract.image_to_string(image_path)
    return text
