import sys
import os

# Adicionar o package ao path para importar corretamente
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from package.models.veiculo import Veiculo

def test_criar_veiculo():
    """Teste para criar um veículo"""
    veiculo = Veiculo("ABC1234", "Gol", "CARRO", "Prata")
    
    assert veiculo.get_placa() == "ABC1234"
    assert veiculo.get_modelo() == "Gol"
    assert veiculo.get_tipo() == "CARRO"
    assert veiculo.get_cor() == "Prata"
    print("✅ test_criar_veiculo: PASSOU")

def test_alterar_placa():
    """Teste para alterar a placa do veículo"""
    veiculo = Veiculo("ABC1234", "Gol", "CARRO", "Prata")
    
    # Alterar placa
    veiculo.set_placa("XYZ9876")
    
    assert veiculo.get_placa() == "XYZ9876"
    print("✅ test_alterar_placa: PASSOU")

def test_alterar_modelo():
    """Teste para alterar o modelo do veículo"""
    veiculo = Veiculo("ABC1234", "Gol", "CARRO", "Prata")
    
    # Alterar modelo
    veiculo.set_modelo("Civic")
    
    assert veiculo.get_modelo() == "Civic"
    print("✅ test_alterar_modelo: PASSOU")

def test_string_representation():
    """Teste para a representação em string do veículo"""
    veiculo = Veiculo("ABC1234", "Gol", "CARRO", "Prata")
    
    resultado = str(veiculo)
    esperado = "ABC1234 - Gol (CARRO)"
    
    assert resultado == esperado
    print("✅ test_string_representation: PASSOU")

def test_diferentes_tipos_veiculo():
    """Teste para criar veículos de diferentes tipos"""
    carro = Veiculo("CAR123", "Gol", "CARRO", "Azul")
    moto = Veiculo("MOT456", "CG", "MOTO", "Vermelha")
    van = Veiculo("VAN789", "Kombi", "VAN", "Branca")
    
    assert carro.get_tipo() == "CARRO"
    assert moto.get_tipo() == "MOTO" 
    assert van.get_tipo() == "VAN"
    print("✅ test_diferentes_tipos_veiculo: PASSOU")

def test_encapsulamento():
    """Teste para verificar encapsulamento (atributos privados)"""
    veiculo = Veiculo("ABC1234", "Gol", "CARRO", "Prata")
    
    # Testar que não podemos acessar atributos privados diretamente
    try:
        # Isso deve falhar se tentarmos acessar diretamente
        placa = veiculo.__placa
        assert False, "❌ Deveria ter falhado - atributo privado acessado"
    except AttributeError:
        print("✅ test_encapsulamento: PASSOU - Atributos estão privados")

if __name__ == "__main__":
    print("🚗 EXECUTANDO TESTES DA CLASSE VEICULO")
    print("=" * 50)
    
    test_criar_veiculo()
    test_alterar_placa()
    test_alterar_modelo()
    test_string_representation()
    test_diferentes_tipos_veiculo()
    test_encapsulamento()
    
    print("=" * 50)
    print("🎉 TODOS OS TESTES DE VEICULO PASSARAM!")