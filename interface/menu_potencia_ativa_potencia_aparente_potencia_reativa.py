from calculos.potencia_ativa import (
    calcular_potencia_ativa_por_potencia_aparente_potencia_reativa,
)
from util.constantes import (
    FORMULA_POTENCIA_ATIVA_POTENCIA_APARENTE_POTENCIA_REATIVA,
    SEPARADOR,
    TITULO_MENU_POTENCIA_ATIVA,
    VOLT_AMPERE,
    VOLT_AMPERE_REATIVO,
)
from util.interface import (
    ler_grandeza,
    mostrar_cabecalho,
    mostrar_erro,
    mostrar_resultado,
    sair_do_menu,
)


def menu_potencia_ativa_potencia_aparente_potencia_reativa():

    while True:
        mostrar_cabecalho(
            TITULO_MENU_POTENCIA_ATIVA,
            FORMULA_POTENCIA_ATIVA_POTENCIA_APARENTE_POTENCIA_REATIVA,
        )

        print(SEPARADOR)

        try:
            potencia_aparente = ler_grandeza("Potência Aparente", VOLT_AMPERE)
            potencia_reativa = ler_grandeza("Potência Reativa", VOLT_AMPERE_REATIVO)

            print(SEPARADOR)

            grandeza, resultado, unidade = (
                calcular_potencia_ativa_por_potencia_aparente_potencia_reativa(
                    potencia_aparente, potencia_reativa
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
