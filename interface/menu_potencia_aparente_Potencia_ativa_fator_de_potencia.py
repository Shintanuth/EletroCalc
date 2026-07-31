from calculos.potencia_aparente import calcular_potencia_aparente_por_potencia_ativa_e_fator_de_potencia
from util.constantes import (
                             SEPARADOR, 
                             TITULO_MENU_POTENCIA_APARENTE, 
                             FORMULA_POTENCIA_APARENTE_POTENCIA_ATIVA_FATOR_DE_POTENCIA, 
                             WATT, 
                            )
from util.interface import (
                            mostrar_cabecalho, 
                            mostrar_resultado, 
                            mostrar_erro, 
                            ler_grandeza, 
                            sair_do_menu
                            )

def menu_potencia_aparente_potencia_ativa_fator_de_potencia():

    while True:

            mostrar_cabecalho(
                TITULO_MENU_POTENCIA_APARENTE,
                FORMULA_POTENCIA_APARENTE_POTENCIA_ATIVA_FATOR_DE_POTENCIA,
            )

            print(SEPARADOR)
            

            try:
                tensao = ler_grandeza("Potência Ativa", WATT)
                corrente = ler_grandeza("Fator de Potências")

                print(SEPARADOR)

                grandeza, resultado, unidade = (calcular_potencia_aparente_por_potencia_ativa_e_fator_de_potencia(tensao, corrente))
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