from datetime import datetime

class Ticket:
    _proximo_id = 1
    
    def __init__(self, veiculo, vaga):
        self.__id = Ticket._proximo_id
        Ticket._proximo_id += 1
        self.__veiculo = veiculo
        self.__vaga = vaga
        self.__entrada = datetime.now()
        self.__saida = None
        self.__valor_pago = 0.0
    
    def calcular_valor(self, taxa_hora):
        if self.__saida is None:
            saida_temp = datetime.now()
        else:
            saida_temp = self.__saida
        
        tempo_permanencia = saida_temp - self.__entrada
        horas = tempo_permanencia.total_seconds() / 3600
        horas = int(horas) + (1 if horas % 1 > 0 else 0)
        
        return max(horas * taxa_hora, taxa_hora)
    
    def finalizar(self, taxa_hora):
        self.__saida = datetime.now()
        self.__valor_pago = self.calcular_valor(taxa_hora)
        return self.__valor_pago
    
    # Getters
    def get_id(self):
        return self.__id
    
    def get_veiculo(self):
        return self.__veiculo
    
    def get_vaga(self):
        return self.__vaga
    
    def get_entrada(self):
        return self.__entrada
    
    def get_saida(self):
        return self.__saida
    
    def get_valor_pago(self):
        return self.__valor_pago
    
    def __str__(self):
        saida_str = self.__saida.strftime("%d/%m/%Y %H:%M") if self.__saida else "EM ABERTO"
        return f"Ticket #{self.__id} - {self.__veiculo.get_placa()}"