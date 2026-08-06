from calculos.potencia_reativa import (
    calcular_potencia_reativa_por_tensao_corrente_angulo,
)
from util.constantes import (
    AMPERE,
    FORMULA_POTENCIA_REATIVA_TENSAO_CORRENTE_ANGULO,
    GRAUS,
    SEPARADOR,
    TITULO_MENU_POTENCIA_REATIVA,
    VOLT,
)
from util.interface import (
    ler_grandeza,
    mostrar_cabecalho,
    mostrar_erro,
    mostrar_resultado,
    sair_do_menu,
)


def menu_potencia_reativa_tensao_corrente_angulo():

    while True:
        mostrar_cabecalho(
            TITULO_MENU_POTENCIA_REATIVA,
            FORMULA_POTENCIA_REATIVA_TENSAO_CORRENTE_ANGULO,
        )

        print(SEPARADOR)

        try:
            tensao = ler_grandeza("Tensão", VOLT)
            corrente = ler_grandeza("Corrente", AMPERE)
            angulo = ler_grandeza("Ângulo", GRAUS)

            print(SEPARADOR)

            grandeza, resultado, unidade = (
                calcular_potencia_reativa_por_tensao_corrente_angulo(
                    tensao, corrente, angulo
                )
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
