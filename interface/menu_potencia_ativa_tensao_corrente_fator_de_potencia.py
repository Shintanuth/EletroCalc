from util.constantes import (
                             TITULO_MENU_POTENCIA_ATIVA, 
                             FORMULA_POTENCIA_ATIVA_TENSAO_CORRENTE_FATOR_DE_POTENCIA,
                             SEPARADOR,
                             WATT,
                             AMPERE
                             )
from util.interface import (
                            mostrar_cabecalho, 
                            ler_grandeza, mostrar_resultado,
                            mostrar_erro,
                            sair_do_menu
                            )
from calculos.potencia_ativa import calcular_potencia_ativa_tensao_corrente_fator_de_potencia

def menu_potencia_ativa_tensao_corrente_fator_de_potencia():

    while True:
    
                mostrar_cabecalho(
                    TITULO_MENU_POTENCIA_ATIVA,
                    FORMULA_POTENCIA_ATIVA_TENSAO_CORRENTE_FATOR_DE_POTENCIA,
                )
    
                print(SEPARADOR)
                
    
                try:
                    tensao = ler_grandeza("Potência Ativa", WATT)
                    corrente = ler_grandeza("Corrente", AMPERE)
                    fator_de_potencia = ler_grandeza("Fator de Potências")
    
                    print(SEPARADOR)
    
                    grandeza, resultado, unidade = (calcular_potencia_ativa_tensao_corrente_fator_de_potencia(tensao, corrente, fator_de_potencia))
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