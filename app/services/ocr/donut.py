# app/services/ocr/donut.py

from app.services.ocr.base_ocr import BaseOCR
from transformers import DonutProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch

class DonutOCR(BaseOCR):
    def __init__(self):
        self.processor = DonutProcessor.from_pretrained("naver-clova-ix/donut-base-finetuned-docvqa")
        self.model = VisionEncoderDecoderModel.from_pretrained("naver-clova-ix/donut-base-finetuned-docvqa")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)

    @property
    def name(self) -> str:
        return "Donut"

    def extract_text(self, image_path: str) -> str:
        image = Image.open(image_path).convert("RGB")

        # Prompt estructurado para la tarea de Document QA
        task_prompt = "<s>"

        # Procesamos la imagen
        pixel_values = self.processor(image, return_tensors="pt").pixel_values.to(self.device)

        # Tokenizamos el prompt
        decoder_input_ids = self.processor.tokenizer(
            task_prompt,
            add_special_tokens=False,
            return_tensors="pt"
        ).input_ids.to(self.device)

        # Generamos la salida
        outputs = self.model.generate(
            pixel_values,
            decoder_input_ids=decoder_input_ids,
            max_length=512,
            num_beams=4,
        )

        # Decodificamos la salida
        result = self.processor.batch_decode(outputs, skip_special_tokens=True)[0]
        return result.strip()
