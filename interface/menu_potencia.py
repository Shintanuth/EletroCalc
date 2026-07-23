from util.converte_entrada import converte_entrada
from util.sair_do_menu import sair_do_menu

def menu_potencia():
    
    while True:
            print("========================================")
            print("            Potência Elétrica           ")
            print("")
            print("                P = E x I               ")
            print("                E = P / I               ")
            print("                I = P / E               ")
            print("========================================")
            print("Digite dois valores e deixe um em branco")

        #     potencia = converte_entrada(input("Potência: "))
        #     tensao = converte_entrada(input("Tensão: "))
        #     corrente = converte_entrada(input("Corrente: "))

        #     print(calcular_potencia(potencia, tensao, corrente))
            opcao = sair_do_menu()
           
            match opcao:
                case "c":
                        continue
                case "v":
                        return
                case "s":
                        return "sair"      