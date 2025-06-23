#DEBEMOS TRAERNOS NUESTRAS LIBRERIAS DE FASTAPI
#Traemos el método FastApi que nos permite crear nuestra Aplicación
from fastapi import FastAPI
#Creamos una variable para la aplicación
app = FastAPI()

#Para que un método sea de un Api debemos decorarlo con GET, POST, etc
#En la decoración se indica el EndPoint de acceso
@app.get("/")
def metodoRoot():
    #Este método puede hacer mil cosas, if, bucles
    #Si el método es para un Api SIEMPRE debe devolver algo
    return {"mensaje": "Hoy es lunes y mañana martes"}






