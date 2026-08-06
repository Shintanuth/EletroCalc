from interface.menu_potencia_reativa_tensao_corrente_angulo import (
    menu_potencia_reativa_tensao_corrente_angulo,
)
from util.constantes import (
    OPCOES_MENU_POTENCIA_REATIVA,
    SELETOR_MENU_POTENCIA_REATIVA,
    TITULO_MENU_POTENCIA_REATIVA,
)
from util.interface import (
    mostrar_cabecalho,
    mostrar_erro,
    mostrar_opcoes,
)
from util.mensagens import ERRO_OPCAO_INVALIDA, MSG_OPCAO
from util.validacoes import validar_opcao


def menu_potencia_reativa():

    while True:
        mostrar_cabecalho(TITULO_MENU_POTENCIA_REATIVA)

        opcao = mostrar_opcoes(OPCOES_MENU_POTENCIA_REATIVA)

        try:
            opcao = input(MSG_OPCAO)

            validar_opcao(opcao, SELETOR_MENU_POTENCIA_REATIVA, ERRO_OPCAO_INVALIDA)

        except ValueError as erro:
            mostrar_erro(erro)
            continue

        match opcao:
            case "1":
                menu_potencia_reativa_tensao_corrente_angulo()
            case "2":
                continue
            case "3":
                continue
            case "c":
                continue
            case "v":
                return
            case "s":
                return "sair"
