from calculos.potencia_ativa import (
    calcular_potencia_ativa_por_tensao_corrente_fator_de_potencia,
)
from util.constantes import (
    AMPERE,
    FORMULA_POTENCIA_ATIVA_TENSAO_CORRENTE_FATOR_DE_POTENCIA,
    SEPARADOR,
    TITULO_MENU_POTENCIA_ATIVA,
    WATT,
)
from util.interface import (
    ler_grandeza,
    mostrar_cabecalho,
    mostrar_erro,
    mostrar_resultado,
    sair_do_menu,
)


def menu_potencia_ativa_tensao_corrente_fator_de_potencia():

    while True:
        mostrar_cabecalho(
            TITULO_MENU_POTENCIA_ATIVA,
            FORMULA_POTENCIA_ATIVA_TENSAO_CORRENTE_FATOR_DE_POTENCIA,
        )

        print(SEPARADOR)

        try:
            tensao = ler_grandeza("Tensão", WATT)
            corrente = ler_grandeza("Corrente", AMPERE)
            fator_de_potencia = ler_grandeza("Fator de Potências")

            print(SEPARADOR)

            grandeza, resultado, unidade = (
                calcular_potencia_ativa_por_tensao_corrente_fator_de_potencia(
                    tensao, corrente, fator_de_potencia
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
