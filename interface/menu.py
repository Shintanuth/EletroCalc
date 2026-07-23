from interface.menu_lei_de_ohm import menu_lei_de_ohm
from interface.menu_potencia import menu_potencia
from interface.menu_reatancia_ind import menu_reatancia_indutiva
from interface.menu_reatancia_cap import menu_reatancia_capacitiva

def menu():
    
    while True:
        print("===========================")
        print("      ELETROCALC v0.1")
        print("===========================")
        print(" 1 - Lei de Ohm")
        print(" 2 - Potência Elétrica")
        print(" 3 - Reatância Indutiva" )
        print(" 4 - Reatância Capacitiva")
        print(" 5 - Impedância")
        print(" 6 - Associação em Série")
        print(" 7 - Associação em Paralelo")
        print("[0] Sair")
        print("===========================")

        opcao = input("Escolha uma opção:")

        match opcao:
            case "0":
                break
            case "1":
                if menu_lei_de_ohm() == "sair":
                    break
            case "2":
                if menu_potencia() == "sair":
                    break
            case "3":
                if menu_reatancia_indutiva() == "sair":
                    break
            case "4":
                if menu_reatancia_capacitiva() == "sair":
                    break
            case "5":
                ...
            case "6":
                ...
            case "7":
                ...
            case _:
                print("Digite uma entrada válida")

    print("Até mais")
            


