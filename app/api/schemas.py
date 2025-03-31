# app/api/schemas.py
from pydantic import BaseModel
from typing import List, Literal

class OCRResponse(BaseModel):
    route: Literal["ocr"]
    ocr_engine: str
    pages_processed: int
    text: List[str]

class LLMResponse(BaseModel):
    route: Literal["llm"]
    message: str
    file: str
