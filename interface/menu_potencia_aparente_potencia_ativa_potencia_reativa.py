from calculos.potencia_aparente import calcular_potencia_aparente_por_potencia_ativa_e_potencia_reativa
from util.constantes import (
                             SEPARADOR, 
                             TITULO_MENU_POTENCIA_APARENTE, 
                             FORMULA_POTENCIA_APARENTE_POTENCIA_ATIVA_POTENCIA_REATIVA, 
                             WATT, 
                             VOLT_AMPERE_REATIVO
                            )
from util.interface import (
                            mostrar_cabecalho, 
                            mostrar_resultado, 
                            mostrar_erro, 
                            ler_grandeza, 
                            sair_do_menu
                            )

def menu_potencia_aparente_potencia_ativa_potencia_reativa():

    while True:

            mostrar_cabecalho(
                TITULO_MENU_POTENCIA_APARENTE,
                FORMULA_POTENCIA_APARENTE_POTENCIA_ATIVA_POTENCIA_REATIVA,
            )

            print(SEPARADOR)
           

            try:
                tensao = ler_grandeza("Potência Ativa", WATT)
                corrente = ler_grandeza("Potência Reativa", VOLT_AMPERE_REATIVO)

                print(SEPARADOR)

                grandeza, resultado, unidade = (calcular_potencia_aparente_por_potencia_ativa_e_potencia_reativa(tensao, corrente))
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
                    