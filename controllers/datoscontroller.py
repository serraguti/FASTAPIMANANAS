from fastapi import APIRouter

#Este objeto es que posteriormente haremos referencia dentro 
#de la clase main.py
router = APIRouter()

#A partir del objeto router se generan los diferentes métodos
@router.get("/pruebas")
def misPruebas():
    return {"data": "Haciendo pruebas de Controllers"}

@router.get("/pruebas/{dato}")
def pruebasDato(dato: str):
    return {"data": "Recibiendo dato en pruebas " + dato}