from util.constantes import (
                             TITULO_MENU_POTENCIAS,
                             OPCOES_MENU_POTENCIAS,
                             SELETOR_MENU_POTENCIAS
                             )
from util.mensagens import (
                            MSG_EM_DESENVOLVIMENTO,
                            MSG_OPCAO,
                            ERRO_OPCAO_INVALIDA,
                            )
from util.interface import (
                            mostrar_cabecalho, 
                            mostrar_opcoes, 
                            mostrar_aviso, 
                            formatar_texto,
                            mostrar_erro
                            )
from util.validacoes import validar_opcao
from interface.menu_potencia_ativa import menu_potencia_ativa
from interface.menu_potencia_aparente import menu_potencia_aparente

def menu_potencias():

    while True:

        mostrar_cabecalho(TITULO_MENU_POTENCIAS)
       
        opcao = mostrar_opcoes(OPCOES_MENU_POTENCIAS)

        try:
            opcao = input(MSG_OPCAO)

            validar_opcao(opcao, SELETOR_MENU_POTENCIAS, ERRO_OPCAO_INVALIDA)

        except ValueError as erro:
            mostrar_erro(erro)
    
        match opcao:
            case "1":
                menu_potencia_ativa()
            case "2":
                print(mostrar_aviso(formatar_texto(MSG_EM_DESENVOLVIMENTO)))
                continue
            case "3":
                menu_potencia_aparente()
            case "4":
                print(mostrar_aviso(formatar_texto(MSG_EM_DESENVOLVIMENTO)))
                continue
            case "c":
                continue
            case "v":
                return
            case "s":
                return "sair"
   