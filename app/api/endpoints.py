# -*- coding: utf-8 -*-
from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.get("/test")
def test_endpoint():
    return {"message": "Endpoint de prueba exitoso"}

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }