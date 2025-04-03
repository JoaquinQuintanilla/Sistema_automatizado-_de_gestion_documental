# app/services/ocr/paddleocr.py

from app.services.ocr.base_ocr import BaseOCR
from paddleocr import PaddleOCR as PaddleOCRBase
from PIL import Image

class PaddleOCRService(BaseOCR):
    def __init__(self):
        self.ocr = PaddleOCRBase(use_angle_cls=True, lang='es')

    @property
    def name(self) -> str:
        return "PaddleOCR"

    def extract_text(self, image_path: str) -> str:
        image = Image.open(image_path).convert("RGB")
        result = self.ocr.ocr(image_path, cls=True)
        textos = []

        for line in result:
            for (_, text_info) in line:
                texto = text_info[0]
                textos.append(texto)

        return "\n".join(textos).strip()
