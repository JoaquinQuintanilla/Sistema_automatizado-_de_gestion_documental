# app/core/config.py
from pydantic_settings import BaseSettings 
from pathlib import Path

class Settings(BaseSettings):
    APP_NAME: str = "Mi API OCR"
    LOG_LEVEL: str = "INFO"
    MAX_FILE_SIZE_MB: int = 5
    OUTPUT_DIR: str = str(Path(__file__).resolve().parent.parent.parent / "output")

    class Config:
        env_file = ".env"

settings = Settings()