from util.sair_do_menu import sair_do_menu
from util.constantes import SEPARADOR, ESPACOS_DOIS, TITULO_MENU_REAT_CAP

def menu_reatancia_capacitiva():
    
    while True:
            print(SEPARADOR)
            print(ESPACOS_DOIS, TITULO_MENU_REAT_CAP)
            print(ESPACOS_DOIS, "Xc = 1 / 2 π x ƒ x C")
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