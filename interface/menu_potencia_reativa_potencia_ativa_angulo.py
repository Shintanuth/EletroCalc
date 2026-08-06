from calculos.potencia_reativa import (
    calcular_potencia_reativa_por_potencia_ativa_angulo,
)
from util.constantes import (
    FORMULA_POTENCIA_REATIVA_POTENCIA_ATIVA_ANGULO,
    GRAUS,
    SEPARADOR,
    TITULO_MENU_POTENCIA_REATIVA,
    WATT,
)
from util.interface import (
    ler_grandeza,
    mostrar_cabecalho,
    mostrar_erro,
    mostrar_resultado,
    sair_do_menu,
)


def menu_potencia_reativa_potencia_ativa_angulo():

    while True:
        mostrar_cabecalho(
            TITULO_MENU_POTENCIA_REATIVA,
            FORMULA_POTENCIA_REATIVA_POTENCIA_ATIVA_ANGULO,
        )

        print(SEPARADOR)

        try:
            potencia_ativa = ler_grandeza("Potência Ativa", WATT)
            angulo = ler_grandeza("Ângulo", GRAUS)

            print(SEPARADOR)

            grandeza, resultado, unidade = (
                calcular_potencia_reativa_por_potencia_ativa_angulo(
                    potencia_ativa, angulo
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
