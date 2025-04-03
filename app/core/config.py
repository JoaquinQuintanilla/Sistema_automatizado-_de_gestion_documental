# app/core/config.py
from pydantic_settings import BaseSettings 

class Settings(BaseSettings):
    APP_NAME: str = "Mi API OCR"
    LOG_LEVEL: str = "INFO"
    MAX_FILE_SIZE_MB: int = 5

    class Config:
        env_file = ".env"

settings = Settings()