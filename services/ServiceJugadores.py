import json
from models.player import Player

def getPlayers():
    #Abrimos el fichero y lo cargamos en memoria
    info = open("./data/jugadores.json")
    json_data = json.load(info)
    salida = []
    #Recorremos todos los jugadores
    for row in json_data["jugadores"]:
        jugador: Player = Player()
        jugador.id = int(row["numero"])
        jugador.nombre = row["nombre"]
        jugador.posicion = row["posicion"]
        jugador.edad = int(row["edad"])
        salida.append(jugador)
    return salida

def findPlayer(idPlayer: int):
    #Abrimos el fichero y lo cargamos en memoria
    info = open("./data/jugadores.json")
    json_data = json.load(info)
    #Recorremos todos los jugadores
    for row in json_data["jugadores"]:
        if (row["numero"] == idPlayer):
            jugador: Player = Player()
            jugador.id = int(row["numero"])
            jugador.nombre = row["nombre"]
            jugador.posicion = row["posicion"]
            jugador.edad = int(row["edad"])
            return jugador
    return None

#METODOS PARA FILTRAR
def searchPlayersAge(edad: int):
    players = getPlayers()
    filtro = list(filter(lambda x: x.edad > edad, players))
    return filtro

#METODOS PARA FILTRAR
def searchPlayersPosition(posicion: str):
    players = getPlayers()
    filtro = list(filter(lambda x: x.posicion.lower() == posicion.lower(), players))
    return filtro