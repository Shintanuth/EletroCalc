from util.sair_do_menu import sair_do_menu
from util import converte_entrada
from util.constantes import SEPARADOR, TITULO_MENU_REAT_IND, FORMULA_REATANCIA_INDUTIVA, HENRY, HERTZ
from util.interface import mostrar_cabecalho, mostrar_resultado, mostrar_erro, ler_entrada
from calculos.reatancia_ind import calcular_reatancia_indutiva


def menu_reatancia_indutiva():
    
    while True:
            
            mostrar_cabecalho(TITULO_MENU_REAT_IND, FORMULA_REATANCIA_INDUTIVA)

            print(SEPARADOR)

            try:
                frequencia = ler_entrada("Frequência", HERTZ)
                indutancia = ler_entrada("Indutância", HENRY)
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