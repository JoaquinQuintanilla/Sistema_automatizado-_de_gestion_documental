# -*- coding: utf-8 -*-
import os
import uuid
import tempfile

from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse

from app.core.logger import logger
from app.core.config import settings
from app.utils.file_utils import save_upload_file, determine_processing_path
from app.services.ocr.tesseract import TesseractOCR

from app.api.schemas import OCRResponse, LLMResponse
from typing import Union

from app.services.llm.llama3 import Llama3Municipal

router = APIRouter()

ALLOWED_TYPES = ["application/pdf", "image/jpeg", "image/png"]

@router.get("/test")
def test_endpoint():
    logger.info("Se accedió al endpoint de prueba")
    return {"message": "Endpoint de prueba exitoso"}

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    tmp_path = None
    try:
        logger.info(f"Inicio de subida: {file.filename} (Tipo: {file.content_type})")

        if file.content_type not in ALLOWED_TYPES:
            logger.warning(f"Tipo no permitido: {file.content_type}")
            raise HTTPException(
                status_code=400,
                detail=f"Tipo de archivo no soportado. Formatos permitidos: PDF, JPEG, PNG"
            )

        contents = await file.read()
        file_size_mb = len(contents) / (1024 * 1024)
        if file_size_mb > settings.MAX_FILE_SIZE_MB:
            logger.warning(f"Archivo demasiado grande: {file_size_mb:.2f} MB")
            raise HTTPException(
                status_code=400,
                detail=f"Archivo excede el límite de {settings.MAX_FILE_SIZE_MB} MB"
            )

        tmp_filename = f"{uuid.uuid4()}_{file.filename}"
        tmp_path = os.path.join(tempfile.gettempdir(), tmp_filename)
        save_upload_file(contents, tmp_path)
        logger.info(f"Archivo guardado temporalmente en: {tmp_path}")

        decision = determine_processing_path(tmp_path, file.content_type)

        if decision["route"] == "ocr":
            logger.info("El archivo será procesado con OCR (Tesseract)")
            ocr = TesseractOCR()
            textos = []

            try:
                for img_path in decision["source"]:
                    texto = ocr.extract_text(img_path)
                    textos.append(texto)

                texto_completo = "\n".join(textos)

                llm = Llama3Municipal()
                resultado = llm.analyze_text(texto_completo)

                return JSONResponse(content={
                    "route": "ocr+llm",
                    "ocr_engine": ocr.name,
                    "llm_engine": llm.name,
                    "pages_processed": len(textos),
                    "llm_output": resultado
                })

            except Exception as e:
                logger.error(f"Error en flujo OCR → LLaMA: {str(e)}", exc_info=True)
                raise HTTPException(status_code=500, detail="Fallo el procesamiento con OCR o LLM")

        elif decision["route"] == "llm":
            logger.info("El archivo contiene texto embebido. Se procesará con LLaMA 3.2")

            # 1. Obtener texto
            if isinstance(decision["source"], list):
                texto = "\n".join(decision["source"])
            else:
                texto = decision["source"]

            # 2. Procesar con LLM
            try:
                llm = Llama3Municipal()
                resultado = llm.analyze_text(texto)
            except Exception as e:
                logger.error(f"Error al procesar con LLaMA: {str(e)}", exc_info=True)
                raise HTTPException(status_code=500, detail="Error al ejecutar el modelo de lenguaje")

            return JSONResponse(content={
                "route": "llm",
                "llm_engine": llm.name,
                "result": resultado
            })


    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        logger.error(f"Error inesperado al procesar {file.filename}: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Ocurrió un error interno al procesar el archivo"
        )
    finally:
        if tmp_path and os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except Exception as cleanup_err:
                logger.warning(f"No se pudo eliminar archivo temporal: {cleanup_err}")
