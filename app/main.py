# -*- coding: utf-8 -*-
from fastapi import FastAPI
from app.core.logger import logger
from app.api import endpoints

def create_app() -> FastAPI:
    """Factory principal de la aplicación (útil para pruebas)."""
    app = FastAPI(
        title="API de Procesamiento automatica de documentos",
        version="1.0.0",
        description="API para procesar documentos con OCR y LLMs"
    )

    # Configuración de routers
    app.include_router(
        endpoints.router,
        prefix="/api/v1",
        tags=["Procesamiento"]
    )

    @app.get("/", include_in_schema=False)
    async def health_check():
        """Endpoint de salud (excluido de la documentación)."""
        logger.info("Health check solicitado")
        return {"status": "ok", "message": "API operativa"}

    logger.info("Aplicación FastAPI iniciada correctamente")
    return app

# Instancia principal (para producción)
app = create_app()