from fastapi import FastAPI,WebSocket
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from Jugador import Jugador
from AdministradorSalas import AdministradorSalas
from Emparejamiento import Emparejamiento
from Cliente import Cliente

app = FastAPI()
app.mount("/client", StaticFiles(directory="../client"), name="client")
emparejamiento = Emparejamiento()
administrarSalas = AdministradorSalas()
conectados : list[Cliente] = {}


@app.get("/")
async def inicio():
    return FileResponse("../client/index.html")

@app.websocket("/ws")
async def websocketEndpoint(ws : WebSocket):
    await ws.accept()
    print("Cliente conectado")
    data = await ws.receive_json()
    print(data)
    
    nombre = data["nombre"]
    jugador = Jugador(nombre)
    cliente = Cliente(ws,jugador)
    conectados[cliente] = cliente
    
    print(f"Bienvenido {nombre}")
    
    while True:
        await ws.receive_json()

@app.post("/buscar-partida")
def buscarPartida(nombre: str):
    jugador = conectados[Cliente(nombre)]

    emparejamiento.agregarJugador(jugador)

    sala = emparejamiento.buscarPartida()

    if sala:
        administrarSalas.salas[sala] = sala
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
    
@app.post("/crear-partida")
def crearPartida(nombre : str):
    jugador = conectados[Cliente(nombre)]


@app.post("/jugar")
def jugar(codigoSala : str, jugador: str,jugada : str):
    sala = administrarSalas.salas.get(codigoSala)

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
        "ganador" : resultado,
        "jugada 1" : sala.eleccionJug1,
        "jugada 2" : sala.eleccionJug2
    }
