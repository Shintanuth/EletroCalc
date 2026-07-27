from util.sair_do_menu import sair_do_menu
from util import converte_entrada
from util.constantes import SEPARADOR, ESPACOS_DOIS, TITULO_MENU_REAT_IND
from util.mostrar_resultado import mostrar_resultado
from util.interface import mostrar_cabecalho
from util.converte_entrada import converte_entrada
from calculos.reatancia_ind import calcular_reatancia_indutiva


def menu_reatancia_indutiva():
    
    while True:
            
            mostrar_cabecalho(TITULO_MENU_REAT_IND)

            print(ESPACOS_DOIS, "XL = (2 x π x ƒ x L)")
            print(SEPARADOR)
            
            try:
                frequencia = converte_entrada(input("Frequência (Hz): "))
                indutancia = converte_entrada(input("Indutância (mH): "))
                print(SEPARADOR)

                grandeza, resultado, unidade = (calcular_reatancia_indutiva(frequencia, indutancia))
                print(mostrar_resultado(grandeza, resultado, unidade))

            except ValueError as erro:
                print(erro)
                   
            

            opcao = sair_do_menu()
            
            match opcao:
                case "c":
                        continue
                case "v":
                        return
                case "s":
                        return "sair"      