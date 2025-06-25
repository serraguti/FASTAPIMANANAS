from fastapi import APIRouter
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
    return api_response(data=player)