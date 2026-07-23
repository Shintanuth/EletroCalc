from interface.menu_lei_de_ohm import menu_lei_de_ohm
from interface.menu_potencia import menu_potencia
from interface.menu_reatancia_ind import menu_reatancia_indutiva
from interface.menu_reatancia_cap import menu_reatancia_capacitiva
from util.constantes import SEPARADOR

def menu():
    
    while True:
        print(SEPARADOR)
        print("            ELETROCALC v0.1")
        print(SEPARADOR)
        print(" 1 - Lei de Ohm")
        print(" 2 - Potência Elétrica")
        print(" 3 - Reatância Indutiva" )
        print(" 4 - Reatância Capacitiva")
        print(" 5 - Impedância")
        print(" 6 - Associação em Série")
        print(" 7 - Associação em Paralelo")
        print("[0] Sair")
        print(SEPARADOR)

        opcao = input("Escolha uma opção: ")

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
                print("Função em desenvolvimento...")
            case "6":
               print("Função em desenvolvimento...")
            case "7":
                print("Função em desenvolvimento...")
            case _:
                print("Digite uma entrada válida")

    print("Até mais")
            


