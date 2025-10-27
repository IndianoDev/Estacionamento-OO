import os
from datetime import datetime

class MenuEstacionamento:
    def __init__(self, estacionamento):
        self.estacionamento = estacionamento
        
    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_cabecalho(self, titulo):
        print("=" * 50)
        print(f"🏢 {self.estacionamento.get_nome()} - {titulo}")
        print("=" * 50)
    
    def aguardar_enter(self):
        input("\nPressione ENTER para continuar...")
    
    def mostrar_menu_principal(self):
        self.limpar_tela()
        self.mostrar_cabecalho("MENU PRINCIPAL")
        
        print("1. Registrar Entrada de Veículo")
        print("2. Registrar Saída de Veículo") 
        print("3. Consultar Veículo por Placa")
        print("4. Visualizar Situação das Vagas")
        print("5. Relatórios e Estatísticas")
        print("6. Gerenciar Veículos")
        print("7. Sair do Sistema")
        print("-" * 30)
    
    def registrar_entrada_veiculo(self):
        self.limpar_tela()
        self.mostrar_cabecalho("REGISTRAR ENTRADA")
        
        print("Informe os dados do veículo:")
        placa = input("Placa: ").upper().strip()
        modelo = input("Modelo: ").strip()
        
        print("\nTipo de veículo:")
        print("1. Carro")
        print("2. Moto")
        print("3. Van")
        
        opcao_tipo = input("Opção (1-3): ").strip()
        tipo_map = {'1': 'CARRO', '2': 'MOTO', '3': 'VAN'}
        tipo_veiculo = tipo_map.get(opcao_tipo, 'CARRO')
        
        cor = input("Cor: ").strip()
        
        ticket = self.estacionamento.registrar_entrada(placa, modelo, tipo_veiculo, cor)
        
        if ticket:
            print(f"\n✅ Entrada registrada com sucesso!")
            print(f"Ticket: #{ticket.get_id()}")
            print(f"Vaga: {ticket.get_vaga().get_numero()}")
        else:
            print("\n❌ Não foi possível registrar a entrada.")
            
        self.aguardar_enter()
    
    def registrar_saida_veiculo(self):
        self.limpar_tela()
        self.mostrar_cabecalho("REGISTRAR SAÍDA")
        
        try:
            ticket_id = int(input("Número do Ticket: "))
            valor = self.estacionamento.registrar_saida(ticket_id)
            
            if valor is not None:
                print(f"\n✅ Saída registrada!")
                print(f"Valor total: R$ {valor:.2f}")
            else:
                print("\n❌ Ticket não encontrado.")
                
        except ValueError:
            print("\n❌ Digite um número válido.")
            
        self.aguardar_enter()
    
    def consultar_veiculo(self):
        self.limpar_tela()
        self.mostrar_cabecalho("CONSULTAR VEÍCULO")
        
        placa = input("Digite a placa: ").upper().strip()
        ticket = self.estacionamento.buscar_veiculo(placa)
        
        if ticket:
            veiculo = ticket.get_veiculo()
            print(f"\n✅ Veículo encontrado:")
            print(f"Placa: {veiculo.get_placa()}")
            print(f"Modelo: {veiculo.get_modelo()}")
            print(f"Cor: {veiculo.get_cor()}")
            print(f"Vaga: {ticket.get_vaga().get_numero()}")
            print(f"Entrada: {ticket.get_entrada().strftime('%d/%m/%Y %H:%M')}")
        else:
            print(f"\n❌ Veículo não encontrado.")
            
        self.aguardar_enter()
    
    def visualizar_vagas(self):
        self.limpar_tela()
        self.mostrar_cabecalho("SITUAÇÃO DAS VAGAS")
        
        print("Vagas disponíveis:")
        print("-" * 40)
        
        for vaga in self.estacionamento._Estacionamento__vagas:
            print(vaga)
        
        relatorio = self.estacionamento.relatorio_ocupacao()
        print(f"\nResumo: {relatorio['vagas_ocupadas']}/{relatorio['total_vagas']} ocupadas")
        
        self.aguardar_enter()
    
    def menu_relatorios(self):
        while True:
            self.limpar_tela()
            self.mostrar_cabecalho("RELATÓRIOS")
            
            print("1. Relatório de Ocupação")
            print("2. Tickets Ativos")
            print("3. Voltar ao Menu Principal")
            print("-" * 30)
            
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == '1':
                self.relatorio_ocupacao_detalhado()
            elif opcao == '2':
                self.listar_tickets_ativos()
            elif opcao == '3':
                break
            else:
                print("Opção inválida!")
                self.aguardar_enter()
    
    def relatorio_ocupacao_detalhado(self):
        self.limpar_tela()
        self.mostrar_cabecalho("RELATÓRIO DETALHADO")
        
        relatorio = self.estacionamento.relatorio_ocupacao()
        
        print(f"Estacionamento: {self.estacionamento.get_nome()}")
        print(f"Taxa por hora: R$ {self.estacionamento.get_taxa_hora():.2f}")
        print(f"Total de vagas: {relatorio['total_vagas']}")
        print(f"Vagas ocupadas: {relatorio['vagas_ocupadas']}")
        print(f"Vagas livres: {relatorio['vagas_livres']}")
        print(f"Taxa de ocupação: {relatorio['taxa_ocupacao']:.1f}%")
        
        self.aguardar_enter()
    
    def listar_tickets_ativos(self):
        self.limpar_tela()
        self.mostrar_cabecalho("TICKETS ATIVOS")
        
        tickets = self.estacionamento._Estacionamento__tickets_ativos
        
        if not tickets:
            print("Nenhum ticket ativo no momento.")
        else:
            for ticket in tickets.values():
                print(ticket)
        
        self.aguardar_enter()
    
    def menu_veiculos(self):
        self.limpar_tela()
        self.mostrar_cabecalho("GERENCIAR VEÍCULOS")
        
        print("Funcionalidade em desenvolvimento...")
        print("Em breve: cadastro de clientes frequentes!")
        
        self.aguardar_enter()
    
    def executar(self):
        while True:
            self.mostrar_menu_principal()
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == '1':
                self.registrar_entrada_veiculo()
            elif opcao == '2':
                self.registrar_saida_veiculo()
            elif opcao == '3':
                self.consultar_veiculo()
            elif opcao == '4':
                self.visualizar_vagas()
            elif opcao == '5':
                self.menu_relatorios()
            elif opcao == '6':
                self.menu_veiculos()
            elif opcao == '7':
                print("\nObrigado por usar nosso sistema!")
                break
            else:
                print("Opção inválida! Tente novamente.")
                self.aguardar_enter()