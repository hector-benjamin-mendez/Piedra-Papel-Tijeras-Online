class LogicaJuego:
    
    @staticmethod
    def determinarGanador(jugada1,jugada2):
        if jugada1 == jugada2:
            return "empate"
        
        formasDeGanar = {
        "piedra" : "tijeras",
        "papel" : "piedra",
        "tijeras" : "papel"            
        }

        if formasDeGanar[jugada1] == jugada2:
            return "jugador1"
        else:
            return "jugador2"

