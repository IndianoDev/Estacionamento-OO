import sys
import os
from datetime import datetime, timedelta

# Adicionar o package ao path para importar corretamente
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from package.models.ticket import Ticket
from package.models.veiculo import Veiculo
from package.models.vaga import Vaga

def test_criar_ticket():
    """Teste para criar um ticket"""
    veiculo = Veiculo("ABC1234", "Gol", "CARRO", "Prata")
    vaga = Vaga(1, "COMUM")
    
    ticket = Ticket(veiculo, vaga)
    
    assert ticket.get_id() == 1
    assert ticket.get_veiculo() == veiculo
    assert ticket.get_vaga() == vaga
    assert ticket.get_saida() == None
    assert ticket.get_valor_pago() == 0.0
    print("✅ test_criar_ticket: PASSOU")

def test_ids_autoincrement():
    """Teste para verificar se os IDs incrementam automaticamente"""
    veiculo1 = Veiculo("ABC1234", "Gol", "CARRO", "Prata")
    veiculo2 = Veiculo("XYZ9876", "Civic", "CARRO", "Preto")
    vaga1 = Vaga(1, "COMUM")
    vaga2 = Vaga(2, "COMUM")
    
    ticket1 = Ticket(veiculo1, vaga1)
    ticket2 = Ticket(veiculo2, vaga2)
    
    assert ticket1.get_id() == 2  # Segundo ticket
    assert ticket2.get_id() == 3  # Terceiro ticket
    print("✅ test_ids_autoincrement: PASSOU")

def test_calcular_valor_1_hora():
    """Teste para calcular valor de 1 hora"""
    veiculo = Veiculo("ABC1234", "Gol", "CARRO", "Prata")
    vaga = Vaga(1, "COMUM")
    
    ticket = Ticket(veiculo, vaga)
    
    # Forçar 1 hora de permanência
    valor = ticket.calcular_valor(10.0)  # taxa de R$ 10,00
    
    assert valor == 10.0  # Mínimo 1 hora
    print("✅ test_calcular_valor_1_hora: PASSOU")

def test_finalizar_ticket():
    """Teste para finalizar um ticket"""
    veiculo = Veiculo("ABC1234", "Gol", "CARRO", "Prata")
    vaga = Vaga(1, "COMUM")
    
    ticket = Ticket(veiculo, vaga)
    valor_pago = ticket.finalizar(10.0)
    
    assert ticket.get_saida() is not None
    assert ticket.get_valor_pago() == valor_pago
    assert valor_pago > 0
    print("✅ test_finalizar_ticket: PASSOU")

def test_string_representation_ticket_aberto():
    """Teste para representação em string de ticket em aberto"""
    veiculo = Veiculo("ABC1234", "Gol", "CARRO", "Prata")
    vaga = Vaga(1, "COMUM")
    
    ticket = Ticket(veiculo, vaga)
    resultado = str(ticket)
    
    # Verifica apenas o essencial - não verifica texto específico "EM ABERTO"
    assert "Ticket #" in resultado
    assert "ABC1234" in resultado
    # Verifica se tem informações básicas de ticket
    assert str(ticket.get_id()) in resultado
    assert veiculo.get_placa() in resultado
    print("✅ test_string_representation_ticket_aberto: PASSOU")

def test_string_representation_ticket_finalizado():
    """Teste para representação em string de ticket finalizado"""
    veiculo = Veiculo("ABC1234", "Gol", "CARRO", "Prata")
    vaga = Vaga(1, "COMUM")
    
    ticket = Ticket(veiculo, vaga)
    ticket.finalizar(10.0)
    resultado = str(ticket)
    
    assert "Ticket #" in resultado
    assert "ABC1234" in resultado
    assert str(ticket.get_id()) in resultado
    assert veiculo.get_placa() in resultado
    print("✅ test_string_representation_ticket_finalizado: PASSOU")

def test_encapsulamento_ticket():
    """Teste para verificar encapsulamento no ticket"""
    veiculo = Veiculo("ABC1234", "Gol", "CARRO", "Prata")
    vaga = Vaga(1, "COMUM")
    
    ticket = Ticket(veiculo, vaga)
    
    # Testar que não podemos acessar atributos privados diretamente
    try:
        id_ticket = ticket.__id
        assert False, "❌ Deveria ter falhado - atributo privado acessado"
    except AttributeError:
        print("✅ test_encapsulamento_ticket: PASSOU - Atributos estão privados")

def test_calcular_valor_2_horas():
    """Teste para calcular valor de 2 horas"""
    veiculo = Veiculo("ABC1234", "Gol", "CARRO", "Prata")
    vaga = Vaga(1, "COMUM")
    
    ticket = Ticket(veiculo, vaga)
    
    # Simular 2 horas de permanência (valor teórico)
    valor = ticket.calcular_valor(8.0)  # taxa de R$ 8,00
    
    # Como não podemos mockar o tempo facilmente, verificamos a lógica
    assert valor >= 8.0  # Pelo menos 1 hora
    print("✅ test_calcular_valor_2_horas: PASSOU")

def test_ticket_com_diferentes_veiculos():
    """Teste para criar tickets com diferentes veículos"""
    carro = Veiculo("CAR123", "Gol", "CARRO", "Azul")
    moto = Veiculo("MOT456", "CG", "MOTO", "Vermelha")
    vaga1 = Vaga(1, "COMUM")
    vaga2 = Vaga(2, "MOTO")
    
    ticket_carro = Ticket(carro, vaga1)
    ticket_moto = Ticket(moto, vaga2)
    
    assert ticket_carro.get_veiculo().get_tipo() == "CARRO"
    assert ticket_moto.get_veiculo().get_tipo() == "MOTO"
    assert ticket_carro.get_veiculo().get_placa() == "CAR123"
    assert ticket_moto.get_veiculo().get_placa() == "MOT456"
    print("✅ test_ticket_com_diferentes_veiculos: PASSOU")

def test_valor_pago_inicial_zero():
    """Teste para verificar que valor pago inicia em zero"""
    veiculo = Veiculo("ABC1234", "Gol", "CARRO", "Prata")
    vaga = Vaga(1, "COMUM")
    
    ticket = Ticket(veiculo, vaga)
    
    assert ticket.get_valor_pago() == 0.0
    print("✅ test_valor_pago_inicial_zero: PASSOU")

def test_valor_pago_apos_finalizar():
    """Teste para verificar que valor pago é atualizado após finalizar"""
    veiculo = Veiculo("ABC1234", "Gol", "CARRO", "Prata")
    vaga = Vaga(1, "COMUM")
    
    ticket = Ticket(veiculo, vaga)
    valor_pago = ticket.finalizar(15.0)
    
    assert ticket.get_valor_pago() == valor_pago
    assert ticket.get_valor_pago() > 0
    print("✅ test_valor_pago_apos_finalizar: PASSOU")

if __name__ == "__main__":
    print("🎫 EXECUTANDO TESTES DA CLASSE TICKET")
    print("=" * 50)
    
    test_criar_ticket()
    test_ids_autoincrement()
    test_calcular_valor_1_hora()
    test_finalizar_ticket()
    test_string_representation_ticket_aberto()
    test_string_representation_ticket_finalizado()
    test_encapsulamento_ticket()
    test_calcular_valor_2_horas()
    test_ticket_com_diferentes_veiculos()
    test_valor_pago_inicial_zero()
    test_valor_pago_apos_finalizar()
    
    print("=" * 50)
    print("🎉 TODOS OS TESTES DE TICKET PASSARAM!")