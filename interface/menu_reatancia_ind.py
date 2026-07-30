from calculos.reatancia_ind import calcular_reatancia_indutiva
from util.constantes import (
                             SEPARADOR, 
                             TITULO_MENU_REAT_IND, 
                             FORMULA_REATANCIA_INDUTIVA, 
                             HENRY, 
                             HERTZ
                             )
from util.interface import (
                            mostrar_cabecalho, 
                            mostrar_resultado, 
                            mostrar_erro, 
                            ler_grandeza, 
                            sair_do_menu
                            )

def menu_reatancia_indutiva():
    
    while True:
            
            mostrar_cabecalho(TITULO_MENU_REAT_IND, FORMULA_REATANCIA_INDUTIVA)

            print(SEPARADOR)

            try:
                frequencia = ler_grandeza("Frequência", HERTZ)
                indutancia = ler_grandeza("Indutância", HENRY)
                print(SEPARADOR)

                grandeza, resultado, unidade = (calcular_reatancia_indutiva(frequencia, indutancia))
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