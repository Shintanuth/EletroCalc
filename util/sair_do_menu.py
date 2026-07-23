def sair_do_menu():
    while True:
        print("============================")
        print("[c] Continuar")
        print("[v] voltar ao menu principal")
        print("[s] sair")
        opcao = input("Digite sua opção: ").strip().lower()
        
        if opcao in ("c","v","s"):
            return opcao

        print("Opção Inválida")