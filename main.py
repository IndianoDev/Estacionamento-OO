from package.models.estacionamento import Estacionamento
from package.utils.menu import MenuEstacionamento

def main():
    estacionamento = Estacionamento("Parking UnB", 15, 10.0)
    menu = MenuEstacionamento(estacionamento)
    
    print("Bem-vindo ao Sistema de Estacionamento!")
    print("Iniciando menu interativo...")
    
    menu.executar()

if __name__ == "__main__":
    main()