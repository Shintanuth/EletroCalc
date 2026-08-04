from calculos.potencia_aparente import (
    calcular_potencia_aparente_por_potencia_ativa_e_potencia_reativa,
)
from util.constantes import (
    FORMULA_POTENCIA_APARENTE_POTENCIA_ATIVA_POTENCIA_REATIVA,
    SEPARADOR,
    TITULO_MENU_POTENCIA_APARENTE,
    VOLT_AMPERE_REATIVO,
    WATT,
)
from util.interface import (
    ler_grandeza,
    mostrar_cabecalho,
    mostrar_erro,
    mostrar_resultado,
    sair_do_menu,
)


def menu_potencia_aparente_potencia_ativa_potencia_reativa():

    while True:
        mostrar_cabecalho(
            TITULO_MENU_POTENCIA_APARENTE,
            FORMULA_POTENCIA_APARENTE_POTENCIA_ATIVA_POTENCIA_REATIVA,
        )

        print(SEPARADOR)

        try:
            potencia_ativa = ler_grandeza("Potência Ativa", WATT)
            potencia_reativa = ler_grandeza("Potência Reativa", VOLT_AMPERE_REATIVO)

            print(SEPARADOR)

            grandeza, resultado, unidade = (
                calcular_potencia_aparente_por_potencia_ativa_e_potencia_reativa(
                    potencia_ativa, potencia_reativa
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
