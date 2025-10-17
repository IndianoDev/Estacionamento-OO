import sys
import os

# Adicionar o package ao path para importar corretamente
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from package.models.estacionamento import Estacionamento
from package.models.veiculo import Veiculo

def test_criar_estacionamento():
    """Teste para criar um estacionamento"""
    estacionamento = Estacionamento("Parking Test", 5, 10.0)
    
    assert estacionamento.get_nome() == "Parking Test"
    assert estacionamento.get_taxa_hora() == 10.0
    assert estacionamento.get_total_vagas() == 5
    print("✅ test_criar_estacionamento: PASSOU")

def test_registrar_entrada():
    """Teste para registrar entrada de veículo"""
    estacionamento = Estacionamento("Parking Test", 5, 10.0)
    ticket = estacionamento.registrar_entrada("TEST123", "Gol", "CARRO", "Azul")
    
    assert ticket is not None
    assert ticket.get_veiculo().get_placa() == "TEST123"
    print("✅ test_registrar_entrada: PASSOU")

def test_entrada_duplicada():
    """Teste para evitar entrada duplicada"""
    estacionamento = Estacionamento("Parking Test", 5, 10.0)
    ticket1 = estacionamento.registrar_entrada("TEST123", "Gol", "CARRO", "Azul")
    ticket2 = estacionamento.registrar_entrada("TEST123", "Gol", "CARRO", "Azul")
    
    assert ticket1 is not None
    assert ticket2 is None  # Segunda entrada deve falhar
    print("✅ test_entrada_duplicada: PASSOU")

def test_relatorio_ocupacao():
    """Teste do relatório de ocupação"""
    estacionamento = Estacionamento("Parking Test", 3, 10.0)
    estacionamento.registrar_entrada("TEST123", "Gol", "CARRO", "Azul")
    
    relatorio = estacionamento.relatorio_ocupacao()
    
    assert relatorio['total_vagas'] == 3
    assert relatorio['vagas_ocupadas'] == 1
    assert relatorio['vagas_livres'] == 2
    print("✅ test_relatorio_ocupacao: PASSOU")

if __name__ == "__main__":
    test_criar_estacionamento()
    test_registrar_entrada()
    test_entrada_duplicada()
    test_relatorio_ocupacao()
    print("\n🎉 TODOS OS TESTES PASSARAM!")