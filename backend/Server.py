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
    nombre = data["nombre"]
    jugador = Jugador(nombre)
    cliente = Cliente(ws,jugador)
    conectados[cliente] = cliente
    
    print(f"Bienvenido {nombre}")
    
    while True:
        data = await ws.receive_json()

        tipo = data["tipo"]

        if tipo == "buscar_partida":
            jugador = Jugador(data["nombre"])
            cliente = Cliente(ws,jugador)
            emparejamiento.agregarJugador(cliente)
            sala = emparejamiento.buscarPartida()

            if sala:
                administrarSalas.salas[sala] = sala
                print(f"Sala creada \n room: {sala.codigo} \njugador 1: {sala.Jugador1.jugador.nombre}\njugador 2: {sala.Jugador2.jugador.nombre}") 
                await sala.Jugador1.ws.send_json({"mensaje" : "¡Rival encontrado!"})
                await sala.Jugador2.ws.send_json({"mensaje":"¡Rival encontrado!"})
            else:
                print(f"{jugador.nombre} está buscando un adversario...")
                await ws.send_json({"mensaje" : "Buscando un rival..."})
