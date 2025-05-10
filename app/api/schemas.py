# app/api/schemas.py
from pydantic import BaseModel
from typing import List, Optional, Literal
from enum import Enum


class OCREngineEnum(str, Enum):
    paddleocr = "paddleocr"

class LLMEngineEnum(str, Enum):
    llama = "llama"
    qwem = "qwen"


class OCRResponse(BaseModel):
    route: Literal["ocr", "ocr+llm"]
    ocr_engine: str
    pages_processed: int
    text: Optional[List[str]] = None
    llm_engine: Optional[str] = None
    llm_output: Optional[dict] = None


class LLMResponse(BaseModel):
    route: Literal["llm"]
    llm_engine: str
    result: dict
