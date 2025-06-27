#DEBEMOS TRAERNOS NUESTRAS LIBRERIAS DE FASTAPI
#Traemos el método FastApi que nos permite crear nuestra Aplicación
from fastapi import FastAPI, Depends
from dependencies.DependencyMethods import dependenciaGlobal1, dependenciaGlobal2
from typing import Union
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import json
from models.player import Player
import services.ServiceJugadores as service
from controllers.datoscontroller import router as datoscontroller
from controllers.jugadorescontroller import router as jugadorescontroller
#Creamos una variable para la aplicación
app = FastAPI(dependencies=[Depends(dependenciaGlobal1)
                            , Depends(dependenciaGlobal2)])

#Tenemos dos opciones en el momento de integrar el controller
#1) Integrar TODO el nuevo controller en la funcionalidad principal
#app.include_router(datoscontroller)
#2) Separar el controller indicando un prefijo para acceder a sus métodos
#y un nombre de controller para la documentación
app.include_router(datoscontroller, prefix="/api", tags=["Datos"])
app.include_router(jugadorescontroller, prefix="/api", tags=["Jugadores"])




#CREAMOS UNA CLASE PARA SER RECIBIDA EN PUT/POST
class Dato(BaseModel):
    nombre: str
    cantidad: int

@app.put("/put")
def updateDato(dato: Dato):
    return {"Nombre recibido": dato.nombre
            , "cantidad": dato.cantidad}

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
def getDoble(numero: int, mensaje: str):
    #INTERNAMENTE NO ES NECESARIO EL TIPADO
    doble: int = numero * 2
    return {"doble": doble,
            "mensaje": mensaje}

@app.get("/saludito")
def dameSaludito(nombre: str, aficion: Union[str, None]=None):
    return {"saludo": "Hola holita " + nombre
            , "aficion": aficion}

@app.get("/numeros")
def dameNumeros():
    listaNumeros = [33,44,55,22,11]
    #Necesitamos convertir cada número a Diccionario: {key:value}
    #salida = [{'numero': 33}]
    #{"\"numero\"": 33}
    salida = []
    for num in listaNumeros:
        #Creamos un diccionario para cada numero
        elemento = {"numero": num}
        item = jsonable_encoder(elemento)
        salida.append(item)
    return {"numeros": salida}





