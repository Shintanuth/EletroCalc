from util.converte_entrada import converte_entrada
from calculos.lei_de_ohm import calcular_lei_de_ohm
from util.sair_do_menu import sair_do_menu
from util.mostrar_resultados import mostrar_resultado_lei_de_ohm

def menu_lei_de_ohm():
    while True:
            print("========================================")
            print("               Lei de Ohm               ")
            print("")
            print("               I = E / R                ")
            print("               E = I x R                ")
            print("               R = E / I                ")
            print("========================================")
            print("Digite dois valores e deixe um em branco")
            print("========================================")

            try:
                tensao = converte_entrada(input("Tensão: "))
                corrente = converte_entrada(input("Corrente: "))
                resistencia = converte_entrada(input("Resistência: "))
                print("====================================")

                grandeza, resultado, unidade = (calcular_lei_de_ohm(tensao, corrente, resistencia))
                print(mostrar_resultado_lei_de_ohm(grandeza, resultado, unidade))

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
                 
           
                    


                    