from calculos.lei_de_ohm import calcular_lei_de_ohm
from util.constantes import (
    AMPERE,
    FORMULA_LEI_DE_OHM,
    OHM,
    SEPARADOR,
    TITULO_MENU_LEI_DE_OHM,
    VOLT,
)
from util.interface import (
    formatar_texto,
    ler_grandeza,
    mostrar_cabecalho,
    mostrar_erro,
    mostrar_resultado,
    sair_do_menu,
)
from util.mensagens import MSG_DOIS_VALORES


def menu_lei_de_ohm():
    while True:
        mostrar_cabecalho(TITULO_MENU_LEI_DE_OHM, FORMULA_LEI_DE_OHM)

        print(SEPARADOR)
        print(formatar_texto(MSG_DOIS_VALORES))
        print(SEPARADOR)

        try:
            tensao = ler_grandeza("Tensão", VOLT)
            corrente = ler_grandeza("Corrente", AMPERE)
            resistencia = ler_grandeza("Resistência", OHM)
            print(SEPARADOR)

            grandeza, resultado, unidade = calcular_lei_de_ohm(
                tensao, corrente, resistencia
            )
            print(mostrar_resultado(grandeza, resultado, unidade))

        except ValueError as erro:
            mostrar_erro(erro)
            continue

        opcao = sair_do_menu()

        match opcao:
            case "c":
                continue
            case "v":
                return
            case "s":
                return "sair"
