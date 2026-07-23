from util.converte_entrada import converte_entrada
from calculos.lei_de_ohm import calcular_lei_de_ohm
from util.sair_do_menu import sair_do_menu
from util.mostrar_resultado import mostrar_resultado
from util.constantes import SEPARADOR

def menu_lei_de_ohm():
    while True:
            print(SEPARADOR)
            print("               Lei de Ohm               ")
            print("")
            print("               I = E / R                ")
            print("               E = I x R                ")
            print("               R = E / I                ")
            print(SEPARADOR)
            print("Digite dois valores e deixe um em branco")
            print(SEPARADOR)

            try:
                tensao = converte_entrada(input("Tensão: "))
                corrente = converte_entrada(input("Corrente: "))
                resistencia = converte_entrada(input("Resistência: "))
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
                 
           
                    


                    