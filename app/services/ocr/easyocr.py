# app/services/ocr/easyocr.py

from app.services.ocr.base_ocr import BaseOCR
import easyocr
from PIL import Image

class EasyOCR(BaseOCR):
    def __init__(self):
        self.reader = easyocr.Reader(['es'], gpu=True)

    @property
    def name(self) -> str:
        return "EasyOCR"

    def extract_text(self, image_path: str) -> str:
        result = self.reader.readtext(image_path, detail=0)
        return "\n".join(result).strip()
