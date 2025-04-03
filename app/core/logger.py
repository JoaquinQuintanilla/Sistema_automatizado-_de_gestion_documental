# -*- coding: utf-8 -*-
import logging
from logging.handlers import RotatingFileHandler
from app.core.config import settings

logger = logging.getLogger(settings.APP_NAME)
logger.setLevel(settings.LOG_LEVEL) 

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Handlers
file_handler = RotatingFileHandler(
    "api.log",
    maxBytes=1000000,
    backupCount=3,
    encoding='utf-8'
)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.info("Logger configurado correctamente")