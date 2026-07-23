from util.converte_entrada import converte_entrada
from util.sair_do_menu import sair_do_menu
from calculos.potencia import calcular_potencia
from util.mostrar_resultado import mostrar_resultado
from util.constantes import SEPARADOR

def menu_potencia():
    
    while True:
            print(SEPARADOR)
            print("            Potência Elétrica           ")
            print("")
            print("                P = E x I               ")
            print("                E = P / I               ")
            print("                I = P / E               ")
            print(SEPARADOR)
            print("Digite dois valores e deixe um em branco")

            try:
                potencia = converte_entrada(input("Potência: "))
                tensao = converte_entrada(input("Tensão: "))
                corrente = converte_entrada(input("Corrente: "))
                print(SEPARADOR)

                grandeza, resultado, unidade = (calcular_potencia(potencia, tensao, corrente))
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