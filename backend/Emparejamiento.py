from Sala import Sala
class Emparejamiento:
    def __init__(self):
        self.cola = []
    
    def agregarJugador(self,jugador):
        self.cola.append(jugador)

    def buscarPartida(self):
        if len(self.cola) >= 2:
            jugador1 = self.cola.pop(0)
            jugador2 = self.cola.pop(0)

            sala = Sala("ABCD123")

            sala.ingresarJugador(jugador1)
            sala.ingresarJugador(jugador2)

            return sala
        return None