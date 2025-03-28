# -*- coding: utf-8 -*-
from fastapi import FastAPI
from app.api import endpoints  # Nueva importación

app = FastAPI()

# Incluir el router
app.include_router(endpoints.router, prefix="/api/v1")

@app.get("/")
def health_check():
    return {"status": "ok", "message": "API inicial funcionando"}