from util.sair_do_menu import sair_do_menu
from util.constantes import TITULO_MENU_POTENCIAS,OPCOES_MENU_POTENCIAS
from util.mensagens import ERRO_OPCAO_INVALIDA
from util.interface import mostrar_cabecalho, mostrar_opcoes
from interface.menu_potencia_ativa import menu_potencia_ativa


def menu_potencias():

    while True:

        mostrar_cabecalho(TITULO_MENU_POTENCIAS)
       
        opcao = mostrar_opcoes(OPCOES_MENU_POTENCIAS)
                   
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
                print(ERRO_OPCAO_INVALIDA)      