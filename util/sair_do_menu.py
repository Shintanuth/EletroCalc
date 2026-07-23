from util.constantes import SEPARADOR

def sair_do_menu():
    while True:
        print(SEPARADOR)
        print("[c] Continuar")
        print("[v] voltar ao menu principal")
        print("[s] sair")
        print(SEPARADOR)
        opcao = input("Digite sua opção: ").strip().lower()
        
        if opcao in ("c","v","s"):
            return opcao

        print("Opção Inválida")