# -*- coding: utf-8 -*-
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.core.logger import logger
from app.core.config import settings

router = APIRouter()

# Tipos de archivo permitidos (podrían moverse a config.py si son configurables)
ALLOWED_TYPES = ["application/pdf", "image/jpeg", "image/png"]

@router.get("/test")
def test_endpoint():
    """Endpoint de prueba para verificar que la API está funcionando."""
    logger.info("Se accedió al endpoint de prueba")
    return {"message": "Endpoint de prueba exitoso"}

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    """
    Procesa archivos subidos (PDF, JPEG, PNG) con validaciones de tipo y tamaño.
    
    Args:
        file (UploadFile): Archivo subido por el usuario.
    
    Returns:
        JSONResponse: Detalles del archivo o mensaje de error.
    """
    try:
        logger.info(f"Inicio de subida: {file.filename} (Tipo: {file.content_type})")
        
        # Validación 1: Tipo de archivo
        if file.content_type not in ALLOWED_TYPES:
            logger.warning(f"Tipo no permitido: {file.content_type}")
            raise HTTPException(
                status_code=400,
                detail=f"Tipo de archivo no soportado. Formatos permitidos: {', '.join(ALLOWED_TYPES)}"
            )
        
        # Validación 2: Tamaño del archivo
        contents = await file.read()
        file_size_mb = len(contents) / (1024 * 1024)
        logger.info(f"Archivo {file.filename} leído - Tamaño: {file_size_mb:.2f} MB")
        
        if file_size_mb > settings.MAX_FILE_SIZE_MB:
            logger.warning(f"Archivo demasiado grande: {file_size_mb:.2f} MB (Máx: {settings.MAX_FILE_SIZE_MB} MB)")
            raise HTTPException(
                status_code=400,
                detail=f"Archivo excede el límite de {settings.MAX_FILE_SIZE_MB} MB"
            )
        
        # Respuesta exitosa
        response_data = {
            "filename": file.filename,
            "content_type": file.content_type,
            "size": f"{file_size_mb:.2f} MB",
            "message": "Archivo validado y listo para procesamiento"
        }
        logger.info(f"Archivo {file.filename} procesado con éxito")
        return JSONResponse(content=response_data, status_code=200)
        
    except HTTPException as http_err:
        # Errores de validación (ya registrados en el logger)
        raise http_err
        
    except Exception as e:
        logger.error(f"Error inesperado al procesar {file.filename}: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Ocurrió un error interno al procesar el archivo"
        )