class Veiculo:
    def __init__(self, placa, modelo, tipo, cor):
        self.__placa = placa
        self.__modelo = modelo
        self.__tipo = tipo
        self.__cor = cor
    
    # Getters
    def get_placa(self):
        return self.__placa
    
    def get_modelo(self):
        return self.__modelo
    
    def get_tipo(self):
        return self.__tipo
    
    def get_cor(self):
        return self.__cor
    
    # Setters
    def set_placa(self, placa):
        self.__placa = placa
    
    def set_modelo(self, modelo):
        self.__modelo = modelo
    
    def __str__(self):
        return f"{self.__placa} - {self.__modelo} ({self.__tipo})"