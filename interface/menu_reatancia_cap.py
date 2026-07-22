def menu_reatancia_capacitiva():
    
    while True:
            print("======================")
            print("Reatância Capacitiva")
            print("Xc = 1 / 2 π x ƒ x C")
            print("======================")



            print("[c] Continuar")
            print("[v] voltar ao menu principal")
            print("[s] sair")
            continuar = input("Digite sua opção: ")

            match continuar:
                    case "c":
                            continue
                    case "v":
                            return
                    case "s":
                            return "sair"
                    case _:
                            print("Opção inválida.")       