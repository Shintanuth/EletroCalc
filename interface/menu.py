from interface.menu_lei_de_ohm import menu_lei_de_ohm

def menu():
    
    while True:
        print("================")
        print("ELETROCALC v0.1")
        print("================")
        print("1 - Lei de Ohm")
        print("2 - Potência Elétrica")
        print("3 - Reatância Indutiva" )
        print("4 - Reatância Capacitiva")
        print("5 - Impedância")
        print("6 - Associação em Série")
        print("7 - Associação em Paralelo")
        print("[0] Sair")
    
        opcao = input("Escolha uma opção:")

        match opcao:
            case "0":
                ...
                break
            case "1":
                menu_lei_de_ohm()
            case "2":
                ...
            case "3":
                ...
            case "4":
                ...
            case "5":
                ...
            case "6":
                ...
            case "7":
                ...
            case _:
                print("Digite uma entrada válida")


