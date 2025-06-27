def parametersInicioFin(inicio: int = 0, fin: int = 30):
    #  AQUI HACEMOS TODO NUESTRO CODIGO, POR EJEMPLO, SANEAR
    #DATOS ANTES DE SER ENVIADOS A LA BBDD
    return {"inicio": inicio, "fin": fin}

def dependenciaGlobal1(token: str):
    print("Dependencia Global 1")

def dependenciaGlobal2():
    print("Dependencia Global 2")