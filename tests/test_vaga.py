import sys
import os

# Adicionar o package ao path para importar corretamente
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from package.models.vaga import Vaga
from package.models.veiculo import Veiculo

def test_criar_vaga():
    """Teste para criar uma vaga"""
    vaga = Vaga(1, "COMUM")
    
    assert vaga.get_numero() == 1
    assert vaga.get_tipo() == "COMUM"
    assert vaga.is_ocupada() == False
    assert vaga.get_veiculo() == None
    print("✅ test_criar_vaga: PASSOU")

def test_ocupar_vaga():
    """Teste para ocupar uma vaga com veículo"""
    vaga = Vaga(1, "COMUM")
    veiculo = Veiculo("ABC1234", "Gol", "CARRO", "Prata")
    
    # Ocupar a vaga
    resultado = vaga.ocupar(veiculo)
    
    assert resultado == True
    assert vaga.is_ocupada() == True
    assert vaga.get_veiculo() == veiculo
    print("✅ test_ocupar_vaga: PASSOU")

def test_ocupar_vaga_ja_ocupada():
    """Teste tentar ocupar vaga já ocupada"""
    vaga = Vaga(1, "COMUM")
    veiculo1 = Veiculo("ABC1234", "Gol", "CARRO", "Prata")
    veiculo2 = Veiculo("XYZ9876", "Civic", "CARRO", "Preto")
    
    # Ocupar pela primeira vez
    vaga.ocupar(veiculo1)
    
    # Tentar ocupar novamente
    resultado = vaga.ocupar(veiculo2)
    
    assert resultado == False  # Deve falhar
    assert vaga.get_veiculo() == veiculo1  # Veículo não mudou
    print("✅ test_ocupar_vaga_ja_ocupada: PASSOU")

def test_liberar_vaga():
    """Teste para liberar uma vaga ocupada"""
    vaga = Vaga(1, "COMUM")
    veiculo = Veiculo("ABC1234", "Gol", "CARRO", "Prata")
    
    # Ocupar e depois liberar
    vaga.ocupar(veiculo)
    veiculo_liberado = vaga.liberar()
    
    assert vaga.is_ocupada() == False
    assert vaga.get_veiculo() == None
    assert veiculo_liberado == veiculo
    print("✅ test_liberar_vaga: PASSOU")

def test_liberar_vaga_ja_livre():
    """Teste para liberar uma vaga já livre"""
    vaga = Vaga(1, "COMUM")
    
    # Liberar vaga já livre
    veiculo_liberado = vaga.liberar()
    
    assert vaga.is_ocupada() == False
    assert veiculo_liberado == None  # Nenhum veículo para liberar
    print("✅ test_liberar_vaga_ja_livre: PASSOU")

def test_string_representation_vaga_livre():
    """Teste para representação em string de vaga livre"""
    vaga = Vaga(5, "PCD")
    
    resultado = str(vaga)
    esperado = "Vaga 5 (PCD): LIVRE"
    
    assert resultado == esperado
    print("✅ test_string_representation_vaga_livre: PASSOU")

def test_string_representation_vaga_ocupada():
    """Teste para representação em string de vaga ocupada"""
    vaga = Vaga(3, "COMUM")
    veiculo = Veiculo("ABC1234", "Gol", "CARRO", "Prata")
    
    vaga.ocupar(veiculo)
    resultado = str(vaga)
    
    assert "Vaga 3 (COMUM): OCUPADA" in resultado
    assert "ABC1234 - Gol (CARRO)" in resultado
    print("✅ test_string_representation_vaga_ocupada: PASSOU")

def test_diferentes_tipos_vaga():
    """Teste para criar vagas de diferentes tipos"""
    vaga_comum = Vaga(1, "COMUM")
    vaga_pcd = Vaga(2, "PCD")
    vaga_idoso = Vaga(3, "IDOSO")
    vaga_moto = Vaga(4, "MOTO")
    
    assert vaga_comum.get_tipo() == "COMUM"
    assert vaga_pcd.get_tipo() == "PCD"
    assert vaga_idoso.get_tipo() == "IDOSO"
    assert vaga_moto.get_tipo() == "MOTO"
    print("✅ test_diferentes_tipos_vaga: PASSOU")

def test_encapsulamento_vaga():
    """Teste para verificar encapsulamento na vaga"""
    vaga = Vaga(1, "COMUM")
    
    # Testar que não podemos acessar atributos privados diretamente
    try:
        numero = vaga.__numero
        assert False, "❌ Deveria ter falhado - atributo privado acessado"
    except AttributeError:
        print("✅ test_encapsulamento_vaga: PASSOU - Atributos estão privados")

if __name__ == "__main__":
    print("🅿️  EXECUTANDO TESTES DA CLASSE VAGA")
    print("=" * 50)
    
    test_criar_vaga()
    test_ocupar_vaga()
    test_ocupar_vaga_ja_ocupada()
    test_liberar_vaga()
    test_liberar_vaga_ja_livre()
    test_string_representation_vaga_livre()
    test_string_representation_vaga_ocupada()
    test_diferentes_tipos_vaga()
    test_encapsulamento_vaga()
    
    print("=" * 50)
    print("🎉 TODOS OS TESTES DE VAGA PASSARAM!")