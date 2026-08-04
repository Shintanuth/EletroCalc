from calculos.reatancia_cap import calcular_reatancia_capacitiva
from util.constantes import (
    FARAD,
    FORMULA_REATANCIA_CAPACITIVA,
    HERTZ,
    SEPARADOR,
    TITULO_MENU_REAT_CAP,
)
from util.interface import (
    ler_grandeza,
    mostrar_cabecalho,
    mostrar_erro,
    mostrar_resultado,
    sair_do_menu,
)


def menu_reatancia_capacitiva():

    while True:
        mostrar_cabecalho(TITULO_MENU_REAT_CAP, FORMULA_REATANCIA_CAPACITIVA)

        print(SEPARADOR)

        try:
            frequencia = ler_grandeza("Frequência", HERTZ)
            capacitancia = ler_grandeza("Capacitância", FARAD)

            print(SEPARADOR)

            grandeza, resultado, unidade = calcular_reatancia_capacitiva(
                frequencia, capacitancia
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
