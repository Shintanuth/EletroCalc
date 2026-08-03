from util.constantes import (
                             TITULO_MENU_POTENCIA_ATIVA, 
                             FORMULA_POTENCIA_ATIVA_POTENCIA_APARENTE_POTENCIA_REATIVA,
                             SEPARADOR,
                             VOLT_AMPERE_REATIVO,
                             VOLT_AMPERE
                             )
from util.interface import (
                            mostrar_cabecalho, 
                            ler_grandeza, mostrar_resultado,
                            mostrar_erro,
                            sair_do_menu
                            )
from calculos.potencia_ativa import calcular_potencia_ativa_potencia_aparente_potencia_reativa

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
    
                    grandeza, resultado, unidade = (calcular_potencia_ativa_potencia_aparente_potencia_reativa(potencia_aparente, potencia_reativa))
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