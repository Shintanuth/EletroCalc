from interface.menu_potencia_aparente_potencia_ativa_fator_de_potencia import (
    menu_potencia_aparente_potencia_ativa_fator_de_potencia,
)
from interface.menu_potencia_aparente_potencia_ativa_potencia_reativa import (
    menu_potencia_aparente_potencia_ativa_potencia_reativa,
)
from interface.menu_potencia_aparente_tensao_corrente import (
    menu_potencia_aparente_tensao_corrente,
)
from util.constantes import (
    OPCOES_MENU_POTENCIA_APARENTE,
    SELETOR_MENU_POTENCIA_APARENTE,
    TITULO_MENU_POTENCIA_APARENTE,
)
from util.interface import (
    mostrar_cabecalho,
    mostrar_erro,
    mostrar_opcoes,
)
from util.mensagens import ERRO_OPCAO_INVALIDA, MSG_OPCAO
from util.validacoes import validar_opcao


def menu_potencia_aparente():

    while True:
        mostrar_cabecalho(TITULO_MENU_POTENCIA_APARENTE)

        opcao = mostrar_opcoes(OPCOES_MENU_POTENCIA_APARENTE)

        try:
            opcao = input(MSG_OPCAO)

            validar_opcao(opcao, SELETOR_MENU_POTENCIA_APARENTE, ERRO_OPCAO_INVALIDA)

        except ValueError as erro:
            mostrar_erro(erro)
            continue

        match opcao:
            case "1":
                menu_potencia_aparente_tensao_corrente()
            case "2":
                menu_potencia_aparente_potencia_ativa_fator_de_potencia()
            case "3":
                menu_potencia_aparente_potencia_ativa_potencia_reativa()
            case "c":
                continue
            case "v":
                return
            case "s":
                return "sair"
