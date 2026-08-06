from interface.menu_potencia_aparente import menu_potencia_aparente
from interface.menu_potencia_ativa import menu_potencia_ativa
from interface.menu_potencia_reativa import menu_potencia_reativa
from util.constantes import (
    OPCOES_MENU_POTENCIAS,
    SELETOR_MENU_POTENCIAS,
    TITULO_MENU_POTENCIAS,
)
from util.interface import (
    formatar_texto,
    mostrar_aviso,
    mostrar_cabecalho,
    mostrar_erro,
    mostrar_opcoes,
)
from util.mensagens import (
    ERRO_OPCAO_INVALIDA,
    MSG_EM_DESENVOLVIMENTO,
    MSG_OPCAO,
)
from util.validacoes import validar_opcao


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
                menu_potencia_reativa()
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
