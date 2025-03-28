# -*- coding: utf-8 -*-
from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_endpoint():
    return {"message": "Endpoint de prueba exitoso"}