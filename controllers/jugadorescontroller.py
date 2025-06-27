from fastapi import APIRouter, HTTPException
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
def playersAge(edad: int):
    players = service.searchPlayersAge(edad)
    return api_response(data=players)

@router.get("/filterposicion/{posicion}")
def playersPosition(posicion: str):
    players = service.searchPlayersPosition(posicion)
    return api_response(data=players)