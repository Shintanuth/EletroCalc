from util.sair_do_menu import sair_do_menu
from util.constantes import SEPARADOR, TITULO_MENU_POTENCIAS, ESPACOS_DOIS
from interface.menu_potencia_ativa import menu_potencia_ativa

def menu_potencias():

    while True:
        print(SEPARADOR)
        print()
        print(ESPACOS_DOIS, TITULO_MENU_POTENCIAS)
        print()
        print(SEPARADOR)
        print("1 - Potência Ativa")
        print("2 - Potência Reativa")
        print("3 - Potência Aparente")
        print("4 - Fator de Potência")
        print()
        print("[v] - Voltar ao menu anterior")
        print("[s] - Sair")
       
        opcao = input("Digite uma opção: ")
                   
        match opcao:
            case "1":
                menu_potencia_ativa()
            case "2":
                print("Função em desenvolvimento")
                return
            case "3":
                print("Função em desenvolvimento")
                return
            case "4":
                print("Função em desenvolvimento")
                return
            case "c":
                continue
            case "v":
                return
            case "s":
                return "sair"
            case _:
                print("Digite uma entrada válida")      