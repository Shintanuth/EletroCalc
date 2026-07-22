from util.converte_entrada import converte_entrada
from calculos.lei_de_ohm import calcular_lei_de_ohm

def menu_lei_de_ohm():
    while True:
            print("======================")
            print("      Lei de Ohm      ")
            print("      I = E / R       ")
            print("      E = I x R       ")
            print("      R = E / I       ")
            print("======================")
            print("Digite dois valores e deixe um em branco")

            tensao = converte_entrada(input("Tensão: "))
            corrente = converte_entrada(input("Corrente: "))
            resistencia = converte_entrada(input("Resistência: "))

            print(calcular_lei_de_ohm(tensao, corrente, resistencia))

            print("[c] Continuar")
            print("[v] voltar ao menu principal")
            print("[s] sair")
            continuar = input("Digite sua opção: ")

            match continuar:
                    case "c":
                            continue
                    case "v":
                            break
                    case "s":
                            print("Até mais")
                            quit()
                    case _:
                            print("Opção inválida.")       
                    


                    