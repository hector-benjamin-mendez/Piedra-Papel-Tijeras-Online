import string
import secrets

class AdministradorSalas:    
    def __init__(self):
        self.salas = {}
        
    def crearCodigoSalas():
        longitud=4
        caracteres = string.ascii_uppercase + string.digits
        codigo = ''.join(secrets.choice(caracteres) for _ in range(longitud))
        return codigo
