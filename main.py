#DEBEMOS TRAERNOS NUESTRAS LIBRERIAS DE FASTAPI
#Traemos el método FastApi que nos permite crear nuestra Aplicación
from fastapi import FastAPI
from typing import Union
#Creamos una variable para la aplicación
app = FastAPI()

#Para que un método sea de un Api debemos decorarlo con GET, POST, etc
#En la decoración se indica el EndPoint de acceso
@app.get("/")
def metodoRoot():
    #Este método puede hacer mil cosas, if, bucles
    #Si el método es para un Api
    return {"mensaje": "Hoy es miercoles"}

@app.get("/saludo")
def metodoSaludo():
    return {"mensaje": "Bienvenido a mi FastApi"}

@app.get("/doble/{numero}")
def getDoble(numero: int):
    #INTERNAMENTE NO ES NECESARIO EL TIPADO
    doble: int = numero * 2
    return {"doble": doble}

@app.get("/saludito")
def dameSaludito(nombre: str, aficion: Union[str, None]=None):
    return {"saludo": "Hola holita " + nombre
            , "aficion": aficion}





