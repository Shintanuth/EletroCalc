from calculos.potencia_reativa import (
    calcular_potencia_reativa_por_potencia_aparente_potencia_ativa,
)
from util.constantes import (
    FORMULA_POTENCIA_REATIVA_POTENCIA_APARENTE_POTENCIA_ATIVA,
    SEPARADOR,
    TITULO_MENU_POTENCIA_REATIVA,
    VOLT_AMPERE,
    WATT,
)
from util.interface import (
    ler_grandeza,
    mostrar_cabecalho,
    mostrar_erro,
    mostrar_resultado,
    sair_do_menu,
)


def menu_potencia_reativa_potencia_aparente_potencia_ativa():

    while True:
        mostrar_cabecalho(
            TITULO_MENU_POTENCIA_REATIVA,
            FORMULA_POTENCIA_REATIVA_POTENCIA_APARENTE_POTENCIA_ATIVA,
        )

        print(SEPARADOR)

        try:
            potencia_aparente = ler_grandeza("Potência Aparente", VOLT_AMPERE)
            potencia_ativa = ler_grandeza("Potência Ativa", WATT)

            print(SEPARADOR)

            grandeza, resultado, unidade = (
                calcular_potencia_reativa_por_potencia_aparente_potencia_ativa(
                    potencia_aparente, potencia_ativa
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
