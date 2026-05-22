from fastapi import WebSocket
from Jugador import Jugador
class Cliente():
    def __init__(self,websocket : WebSocket, jugador : Jugador):
        self.ws = websocket
        self.jugador = jugador
