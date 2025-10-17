from package.models.veiculo import Veiculo

class Vaga:
    def __init__(self, numero, tipo):
        self.__numero = numero
        self.__tipo = tipo
        self.__ocupada = False
        self.__veiculo = None
    
    def ocupar(self, veiculo):
        if not self.__ocupada:
            self.__ocupada = True
            self.__veiculo = veiculo
            return True
        return False
    
    def liberar(self):
        self.__ocupada = False
        veiculo_liberado = self.__veiculo
        self.__veiculo = None
        return veiculo_liberado
    
    # Getters
    def get_numero(self):
        return self.__numero
    
    def get_tipo(self):
        return self.__tipo
    
    def is_ocupada(self):
        return self.__ocupada
    
    def get_veiculo(self):
        return self.__veiculo
    
    def __str__(self):
        status = "OCUPADA" if self.__ocupada else "LIVRE"
        veiculo_info = f" - {self.__veiculo}" if self.__ocupada else ""
        return f"Vaga {self.__numero} ({self.__tipo}): {status}{veiculo_info}"