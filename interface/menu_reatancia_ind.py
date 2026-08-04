from calculos.reatancia_ind import calcular_reatancia_indutiva
from util.constantes import (
    FORMULA_REATANCIA_INDUTIVA,
    HENRY,
    HERTZ,
    SEPARADOR,
    TITULO_MENU_REAT_IND,
)
from util.interface import (
    ler_grandeza,
    mostrar_cabecalho,
    mostrar_erro,
    mostrar_resultado,
    sair_do_menu,
)


def menu_reatancia_indutiva():

    while True:
        mostrar_cabecalho(TITULO_MENU_REAT_IND, FORMULA_REATANCIA_INDUTIVA)

        print(SEPARADOR)

        try:
            frequencia = ler_grandeza("Frequência", HERTZ)
            indutancia = ler_grandeza("Indutância", HENRY)
            print(SEPARADOR)

            grandeza, resultado, unidade = calcular_reatancia_indutiva(
                frequencia, indutancia
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
