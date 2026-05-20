from LogicaJuego import LogicaJuego
class Sala:    
    def __init__(self,codigo):
        self.codigo = codigo
        self.Jugador1 = None
        self.Jugador2 = None
        self.eleccionJug1 = None
        self.eleccionJug2 = None
        self.estado = "vacia"


    def verificarEstado(self):
        if self.Jugador1 == None and self.Jugador2 == None:
            self.estado = "vacia"
        elif self.Jugador1 != None and self.Jugador2 != None:
            self.estado = "juego"
        else:
            self.estado = "esperando"

    def ingresarJugador(self,Jugador):
        if self.Jugador1 == None:
            self.Jugador1 = Jugador
        else:
            self.Jugador2 = Jugador

    def jugar(self):
        if self.eleccionJug1 != None and self.eleccionJug2 != None:
            resultado = LogicaJuego.determinarGanador(self.eleccionJug1,self.eleccionJug2)
            return resultado
        else:
            return None
