from package.models.vaga import Vaga
from package.models.veiculo import Veiculo
from package.models.ticket import Ticket

class Estacionamento:
    def __init__(self, nome, total_vagas, taxa_hora):
        self.__nome = nome
        self.__taxa_hora = taxa_hora
        self.__vagas = []
        self.__tickets_ativos = {}
        self.__historico = []
        
        # Inicializar vagas
        for i in range(total_vagas):
            tipo = "COMUM"
            if i < 2: tipo = "PCD"
            elif i < 4: tipo = "IDOSO"
            elif i >= total_vagas - 5: tipo = "MOTO"
            
            self.__vagas.append(Vaga(i + 1, tipo))
    
    def registrar_entrada(self, placa, modelo, tipo_veiculo, cor):
        # Verificar se veículo já está estacionado
        for ticket in self.__tickets_ativos.values():
            if ticket.get_veiculo().get_placa() == placa:
                print(f"❌ Veículo {placa} já está estacionado!")
                return None
        
        # Encontrar vaga disponível
        vaga_disponivel = None
        for vaga in self.__vagas:
            if not vaga.is_ocupada() and self.__vaga_compativel(vaga, tipo_veiculo):
                vaga_disponivel = vaga
                break
        
        if vaga_disponivel:
            veiculo = Veiculo(placa, modelo, tipo_veiculo, cor)
            vaga_disponivel.ocupar(veiculo)
            ticket = Ticket(veiculo, vaga_disponivel)
            self.__tickets_ativos[ticket.get_id()] = ticket
            print(f"✅ Entrada registrada - {veiculo} na {vaga_disponivel}")
            return ticket
        else:
            print(f"❌ Nenhuma vaga disponível para {tipo_veiculo}")
            return None
    
    def registrar_saida(self, ticket_id):
        if ticket_id in self.__tickets_ativos:
            ticket = self.__tickets_ativos[ticket_id]
            valor = ticket.finalizar(self.__taxa_hora)
            ticket.get_vaga().liberar()
            del self.__tickets_ativos[ticket_id]
            self.__historico.append(ticket)
            print(f"✅ Saída registrada - Ticket #{ticket_id} - Valor: R$ {valor:.2f}")
            return valor
        else:
            print(f"❌ Ticket #{ticket_id} não encontrado!")
            return None
    
    def __vaga_compativel(self, vaga, tipo_veiculo):
        if vaga.get_tipo() == "MOTO" and tipo_veiculo != "MOTO":
            return False
        return True
    
    def relatorio_ocupacao(self):
        vagas_ocupadas = sum(1 for vaga in self.__vagas if vaga.is_ocupada())
        return {
            'total_vagas': len(self.__vagas),
            'vagas_ocupadas': vagas_ocupadas,
            'vagas_livres': len(self.__vagas) - vagas_ocupadas,
            'taxa_ocupacao': (vagas_ocupadas / len(self.__vagas)) * 100
        }
    
    def buscar_veiculo(self, placa):
        for ticket in self.__tickets_ativos.values():
            if ticket.get_veiculo().get_placa() == placa:
                return ticket
        return None
    
    def listar_vagas(self):
        for vaga in self.__vagas:
            print(vaga)
    
    def listar_tickets_ativos(self):
        for ticket in self.__tickets_ativos.values():
            print(ticket)
    
   
    def get_nome(self):
        return self.__nome
    
    def get_taxa_hora(self):
        return self.__taxa_hora
    
    def get_total_vagas(self):
        return len(self.__vagas)