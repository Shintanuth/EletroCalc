from util.constantes import (
                             TITULO_MENU_POTENCIA_ATIVA, 
                             FORMULA_POTENCIA_ATIVA_POTENCIA_APARENTE_FATOR_DE_POTENCIA,
                             SEPARADOR,
                             VOLT_AMPERE
                             )
from util.interface import (
                            mostrar_cabecalho, 
                            ler_grandeza, mostrar_resultado,
                            mostrar_erro,
                            sair_do_menu
                            )
from calculos.potencia_ativa import calcular_potencia_ativa_por_potencia_aparente_fator_de_potencia

def menu_potencia_ativa_potencia_aparente_fator_de_potencia():

    while True:
    
                mostrar_cabecalho(
                    TITULO_MENU_POTENCIA_ATIVA,
                    FORMULA_POTENCIA_ATIVA_POTENCIA_APARENTE_FATOR_DE_POTENCIA,
                )
    
                print(SEPARADOR)
                
    
                try:
                    potencia_aparente = ler_grandeza("Potência Aparente", VOLT_AMPERE)
                    fator_de_potencia = ler_grandeza("Fator de Potências")
    
                    print(SEPARADOR)
    
                    grandeza, resultado, unidade = (calcular_potencia_ativa_por_potencia_aparente_fator_de_potencia(potencia_aparente, fator_de_potencia))
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