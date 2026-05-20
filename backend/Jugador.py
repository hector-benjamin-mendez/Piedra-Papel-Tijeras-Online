class Jugador:
    
    def __init__(self,nombre):
        self.nombre = nombre
        self.jugada = None
        self.vidas = None

    def crearNombre(self,nombre):
        self.nombre = nombre

    def obtenerNombreJugador(self):
        return self.nombre

    def realizarJugada(self,jugada):
        self.jugada = jugada

    def mostrarJugada(self):
        return self.jugada
    
