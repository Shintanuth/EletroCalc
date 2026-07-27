from util.sair_do_menu import sair_do_menu
from util.constantes import TITULO_MENU_POTENCIAS, ESPACOS_DOIS
from util.interface import mostrar_cabecalho
from interface.menu_potencia_ativa import menu_potencia_ativa


def menu_potencias():

    while True:

        mostrar_cabecalho(TITULO_MENU_POTENCIAS)
       
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
                continue
            case "3":
                print("Função em desenvolvimento")
                continue
            case "4":
                print("Função em desenvolvimento")
                continue
            case "c":
                continue
            case "v":
                return
            case "s":
                return "sair"
            case _:
                print("Digite uma entrada válida")      