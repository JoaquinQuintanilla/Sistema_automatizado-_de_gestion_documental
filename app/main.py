# -*- coding: utf-8 -*-
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok", "message": "API inicial funcionando"}