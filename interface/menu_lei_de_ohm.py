from util.converte_entrada import converte_entrada
from calculos.lei_de_ohm import calcular_lei_de_ohm
from util.sair_do_menu import sair_do_menu
from util.mostrar_resultado import mostrar_resultado
from util.constantes import SEPARADOR, ESPACOS, TITULO_MENU_LEI_DE_OHM
from util.mensagens import MSG_DOIS_VALORES

def menu_lei_de_ohm():
    while True:
            print(SEPARADOR)
            print(ESPACOS, TITULO_MENU_LEI_DE_OHM)
            print()
            print(ESPACOS, "I = E / R")
            print(ESPACOS, "E = I x R")
            print(ESPACOS, "R = E / I")
            print(SEPARADOR)
            print(MSG_DOIS_VALORES)
            print(SEPARADOR)

            try:
                tensao = converte_entrada(input("Tensão (V): "))
                corrente = converte_entrada(input("Corrente (A): "))
                resistencia = converte_entrada(input("Resistência (Ω): "))
                print(SEPARADOR)

                grandeza, resultado, unidade = (calcular_lei_de_ohm(tensao, corrente, resistencia))
                print(mostrar_resultado(grandeza, resultado, unidade))

            except ValueError as erro:
                print(erro)
                continue
                
            
            opcao = sair_do_menu()

            match opcao:
                 case "c":
                       continue
                 case "v":
                      return
                 case "s":
                      return "sair"
                 
           
                    


                    