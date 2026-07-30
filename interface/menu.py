from interface.menu_lei_de_ohm import menu_lei_de_ohm
from interface.menu_potencia import menu_potencias
from interface.menu_reatancia_ind import menu_reatancia_indutiva
from interface.menu_reatancia_cap import menu_reatancia_capacitiva
from util.interface import (
                            mostrar_cabecalho, 
                            mostrar_opcoes , 
                            formatar_texto, 
                            mostrar_erro
                            )
from util.validacoes import validar_opcao
from util.constantes import (
                             TITULO_MENU_PRINCIPAL, 
                             OPCOES_MENU_PRINCIPAL, 
                             VERSAO, 
                             SELETOR_MENU_PRINCIPAL
                             )
from util.mensagens import (
                            MSG_FIM, 
                            MSG_OPCAO, 
                            ERRO_OPCAO_INVALIDA, 
                            TITULO_ERRO
                            )

def menu():
    
    while True:

        mostrar_cabecalho(TITULO_MENU_PRINCIPAL, versao=VERSAO)

        mostrar_opcoes(OPCOES_MENU_PRINCIPAL, voltar=False)

        try:
            opcao = input(MSG_OPCAO)

            validar_opcao(opcao, SELETOR_MENU_PRINCIPAL, ERRO_OPCAO_INVALIDA)

        except ValueError as erro:
            mostrar_erro(TITULO_ERRO, erro)
            continue

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

    print(formatar_texto(MSG_FIM))
            


