from calculos.potencia_aparente import calcular_potencia_aparente_por_tensao_e_corrente
from util.constantes import (
    AMPERE,
    FORMULA_POTENCIA_APARENTE_TENSAO_CORRENTE,
    SEPARADOR,
    TITULO_MENU_POTENCIA_APARENTE,
    VOLT,
)
from util.interface import (
    ler_grandeza,
    mostrar_cabecalho,
    mostrar_erro,
    mostrar_resultado,
    sair_do_menu,
)


def menu_potencia_aparente_tensao_corrente():

    while True:
        mostrar_cabecalho(
            TITULO_MENU_POTENCIA_APARENTE,
            FORMULA_POTENCIA_APARENTE_TENSAO_CORRENTE,
        )

        print(SEPARADOR)

        try:
            tensao = ler_grandeza("Tensão", VOLT)
            corrente = ler_grandeza("Corrente", AMPERE)

            print(SEPARADOR)

            grandeza, resultado, unidade = (
                calcular_potencia_aparente_por_tensao_e_corrente(tensao, corrente)
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
