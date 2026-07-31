from calculos.potencia_aparente import calcular_potencia_aparente_por_tensao_e_corrente
from util.mensagens import MSG_DOIS_VALORES
from util.constantes import (
                             SEPARADOR, 
                             TITULO_MENU_POTENCIA_APARENTE, 
                             FORMULA_POTENCIA_APARENTE_TENSAO_CORRENTE, 
                             VOLT, 
                             AMPERE,
                             VOLT_AMPERE 
                            )
from util.interface import (
                            mostrar_cabecalho, 
                            mostrar_resultado, 
                            mostrar_erro, 
                            ler_grandeza, 
                            sair_do_menu, 
                            formatar_texto
                            )

def menu_potencia_aparente_tensao_corrente():

    while True:

            mostrar_cabecalho(
                TITULO_MENU_POTENCIA_APARENTE,
                FORMULA_POTENCIA_APARENTE_TENSAO_CORRENTE,
            )

            print(SEPARADOR)
            print(formatar_texto(MSG_DOIS_VALORES))
            print(SEPARADOR)

            try:
                tensao = ler_grandeza("Tensão", VOLT)
                corrente = ler_grandeza("Corrente", AMPERE)

                print(SEPARADOR)

                grandeza, resultado, unidade = (calcular_potencia_aparente_por_tensao_e_corrente(tensao, corrente))
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
                    
            
                    
