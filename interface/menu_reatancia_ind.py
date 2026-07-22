def menu_reatancia_indutiva():
    
    while True:
            print("======================")
            print(" Reataância Indutiva ")
            print("  XL = 2 x π x ƒ x L ")
            print("======================")
            print("Digite dois valores e deixe um em branco")

        #     potencia = converte_entrada(input("Potência: "))
        #     tensao = converte_entrada(input("Tensão: "))
        #     corrente = converte_entrada(input("Corrente: "))

        #     print(calcular_potencia(potencia, tensao, corrente))

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