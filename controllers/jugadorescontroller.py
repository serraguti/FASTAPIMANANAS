from fastapi import APIRouter, HTTPException, Depends
from dependencies.DependencyMethods import parametersInicioFin
import services.ServiceJugadores as service
from utils.response_wrapper import api_response

router = APIRouter()

@router.get("/players")
def readPlayers():
    players = service.getPlayers()
    return api_response(data=players, message="todos los jugadores correctos")

@router.get("/findplayer/{idplayer}")
def findPlayer(idplayer: int):
    player = service.findPlayer(idplayer)
    if (player is None):
        raise HTTPException(status_code=404, detail=f"player no found {idplayer}")
    else:
        return api_response(data=player)
    
@router.get("/filteredad/{edad}")
def playersAge(edad: int, commons: dict = Depends(parametersInicioFin)):
    players = service.searchPlayersAge(edad, commons["inicio"], commons["fin"])
    return api_response(data=players)

@router.get("/filterposicion/{posicion}")
def playersPosition(posicion: str,  commons: dict = Depends(parametersInicioFin)):
    players = service.searchPlayersPosition(posicion, commons["inicio"], commons["fin"])
    return api_response(data=players)

@router.get("/filterplayers")
def playersFilter( commons: dict = Depends(parametersInicioFin)):
    players = service.filtrarJugadores(commons["inicio"], commons["fin"])
    return api_response(data=players)