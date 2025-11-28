from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

from app.validator import dividir


class DivisionRequest(BaseModel):
    numero_a: int
    numero_b: int


class DivisionResponse(BaseModel):
    resultado: int


app = FastAPI(title="Base Converter Service")


@app.post("/division", response_model=DivisionResponse)
async def suma(req: DivisionRequest):
    try:
        resultado = dividir(
            req.numero_a,
            req.numero_b
        )
        return DivisionResponse(resultado=resultado)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
