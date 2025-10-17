#!/usr/bin/env python3
"""
Sistema de Controle de Estacionamento
Arquivo principal - Test Bench
"""

from package.models.estacionamento import Estacionamento

def test_bench_completo():
    print("=" * 60)
    print("🧪 TEST BENCH - SISTEMA DE ESTACIONAMENTO")
    print("=" * 60)
    
    # Criar estacionamento
    estacionamento = Estacionamento("Parking UnB", 10, 8.0)
    print(f"🏢 {estacionamento.get_nome()} criado!")
    print(f"💰 Taxa por hora: R$ {estacionamento.get_taxa_hora():.2f}")
    print()
    
    # Registrar entradas
    print("📥 REGISTRANDO ENTRADAS:")
    print("-" * 40)
    
    ticket1 = estacionamento.registrar_entrada("ABC1234", "Gol", "CARRO", "Prata")
    ticket2 = estacionamento.registrar_entrada("XYZ9876", "CG", "MOTO", "Vermelha")
    ticket3 = estacionamento.registrar_entrada("DEF5678", "Civic", "CARRO", "Preto")
    
    print()
    
    # Listar vagas
    print("🅿️  SITUAÇÃO DAS VAGAS:")
    print("-" * 40)
    estacionamento.listar_vagas()
    print()
    
    # Relatório
    print("📊 RELATÓRIO DE OCUPAÇÃO:")
    print("-" * 40)
    relatorio = estacionamento.relatorio_ocupacao()
    print(f"Total de vagas: {relatorio['total_vagas']}")
    print(f"Vagas ocupadas: {relatorio['vagas_ocupadas']}")
    print(f"Vagas livres: {relatorio['vagas_livres']}")
    print(f"Taxa de ocupação: {relatorio['taxa_ocupacao']:.1f}%")
    print()
    
    # Registrar saídas
    print("📤 REGISTRANDO SAÍDAS:")
    print("-" * 40)
    if ticket1:
        estacionamento.registrar_saida(ticket1.get_id())
    
    print()
    
    # Situação final
    print("🅿️  SITUAÇÃO FINAL:")
    print("-" * 40)
    estacionamento.listar_vagas()
    
    print("\n" + "=" * 60)
    print("✅ TEST BENCH CONCLUÍDO COM SUCESSO!")
    print("=" * 60)

if __name__ == "__main__":
    test_bench_completo()