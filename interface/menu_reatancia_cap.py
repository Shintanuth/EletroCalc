from util.sair_do_menu import sair_do_menu
from util.constantes import SEPARADOR

def menu_reatancia_capacitiva():
    
    while True:
            print(SEPARADOR)
            print("     Reatância Capacitiva")
            print("     Xc = 1 / 2 π x ƒ x C")
            print(SEPARADOR)


            print(SEPARADOR)

            opcao = sair_do_menu()
            
            match opcao:
                case "c":
                        continue
                case "v":
                        return
                case "s":
                        return "sair"   