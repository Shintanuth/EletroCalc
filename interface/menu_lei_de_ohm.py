def menu_lei_de_ohm():
    while True:
            print("======================")
            print("      Lei de Ohm      ")
            print("      I = E / R       ")
            print("      E = I x R       ")
            print("      R = E / I       ")
            print("======================")
            print("Digite dois valores e deixe um em branco")

            ...

            print("[c] Continuar")
            print("[v] voltar ao menu principal")
            print("[s] sair")
            continuar = input("Digite sua opção: ")

            match continuar:
                    case "c":
                            ...
                    case "v":
                            break
                    case "s":
                            print("Até mais")
                            return 0
                    


                    