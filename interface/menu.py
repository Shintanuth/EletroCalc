from interface.menu_lei_de_ohm import menu_lei_de_ohm
from interface.menu_potencia import menu_potencias
from interface.menu_reatancia_ind import menu_reatancia_indutiva
from interface.menu_reatancia_cap import menu_reatancia_capacitiva
from util.interface import mostrar_cabecalho, mostrar_opcoes
from util.constantes import TITULO_MENU_PRINCIPAL, OPCOES_MENU_PRINCIPAL, VERSAO
from util.mensagens import MSG_FIM, ERRO_OPCAO_INVALIDA

def menu():
    
    while True:

        mostrar_cabecalho(TITULO_MENU_PRINCIPAL, versao=VERSAO)

        opcao = mostrar_opcoes(OPCOES_MENU_PRINCIPAL, voltar=False)

        match opcao:
            case "s":
                break
            case "1":
                if menu_lei_de_ohm() == "sair":
                    break
            case "2":
                if menu_potencias() == "sair":
                    break
            case "3":
                if menu_reatancia_indutiva() == "sair":
                    break
            case "4":
                if menu_reatancia_capacitiva() == "sair":
                    break
            case _:
                print(ERRO_OPCAO_INVALIDA)

    print(MSG_FIM)
            


