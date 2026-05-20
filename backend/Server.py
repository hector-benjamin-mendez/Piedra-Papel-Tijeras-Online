from fastapi import FastAPI
from Jugador import Jugador
from Emparejamiento import Emparejamiento
from LogicaJuego import LogicaJuego
app = FastAPI()

emparejamiento = Emparejamiento()
salas = {}

@app.post("/buscar-partida")
def buscarPartida(nombre: str):
    jugador = Jugador(nombre)

    emparejamiento.agregarJugador(jugador)

    sala = emparejamiento.buscarPartida()

    if sala:
        salas[sala.codigo] = sala
        print(f"Sala creada\nRoom: {sala.codigo}\nJugador 1: {sala.Jugador1.nombre}\nJugador 2: {sala.Jugador2.nombre}")
        return {
            "mensaje" : "Sala creada",
            "room" : sala.codigo,
            "jugador1" : sala.Jugador1.nombre,
            "jugador2" : sala.Jugador2.nombre

        }

    else:
        print(f"Esperando jugador...")
        return {
            "mensaje" : "esperando jugador..."
        }    
@app.post("/jugar")
def jugar(codigoSala : str, jugador: str,jugada : str):
    sala = salas.get(codigoSala)

    if not sala:
        return {
            "error" : "sala no encontrada. "
        }

    if sala.Jugador1.nombre == jugador:
        sala.eleccionJug1 = jugada
    elif sala.Jugador2.nombre == jugador:
        sala.eleccionJug2 = jugada
    else:
        return {
            "error" : "jugador no encontrado."
        }
    resultado = sala.jugar()

    if resultado is None:
        return{
            "mensaje": "esperando al otro jugador..."
        }

    return {
        "resultado" : resultado,
        "jugada 1" : sala.eleccionJug1,
        "jugada 2" : sala.eleccionJug2
    }
