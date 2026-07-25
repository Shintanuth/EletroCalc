from util.sair_do_menu import sair_do_menu
from util.constantes import SEPARADOR, ESPACOS_DOIS, TITULO_MENU_REAT_CAP
from util.converte_entrada import converte_entrada
from util.mostrar_resultado import mostrar_resultado
from calculos.reatancia_cap import calcular_reatancia_capacitiva

def menu_reatancia_capacitiva():
    
    while True:
            print(SEPARADOR)
            print(ESPACOS_DOIS, TITULO_MENU_REAT_CAP)
            print(ESPACOS_DOIS, "Xc = 1 / (2 π x ƒ x C)")
            print(SEPARADOR)
            try:
                frequencia = converte_entrada(input("Frequência: "))
                capacitancia = converte_entrada(input("Capacitância: "))
                print(SEPARADOR)
            
                grandeza, resultado, unidade = (calcular_reatancia_capacitiva(frequencia, capacitancia))
                print(mostrar_resultado(grandeza, resultado, unidade))
            
            except ValueError as erro:
                print(erro)    

            print(SEPARADOR)

            opcao = sair_do_menu()
            
            match opcao:
                case "c":
                        continue
                case "v":
                        return
                case "s":
                        return "sair"   