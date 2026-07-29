from util.constantes import TITULO_MENU_POTENCIAS,OPCOES_MENU_POTENCIAS
from util.mensagens import MSG_OPCAO_INVALIDA, MSG_EM_DESENVOLVIMENTO
from util.interface import mostrar_cabecalho, mostrar_opcoes, mostrar_aviso, formatar_texto
from interface.menu_potencia_ativa import menu_potencia_ativa


def menu_potencias():

    while True:

        mostrar_cabecalho(TITULO_MENU_POTENCIAS)
       
        opcao = mostrar_opcoes(OPCOES_MENU_POTENCIAS)
                   
        match opcao:
            case "1":
                menu_potencia_ativa()
            case "2":
                print(mostrar_aviso(formatar_texto(MSG_EM_DESENVOLVIMENTO)))
                continue
            case "3":
                print(mostrar_aviso(formatar_texto(MSG_EM_DESENVOLVIMENTO)))
                continue
            case "4":
                print(mostrar_aviso(formatar_texto(MSG_EM_DESENVOLVIMENTO)))
                continue
            case "c":
                continue
            case "v":
                return
            case "s":
                return "sair"
            case _:
                print(MSG_OPCAO_INVALIDA)      