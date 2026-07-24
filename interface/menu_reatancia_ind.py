from util.sair_do_menu import sair_do_menu
from util.constantes import SEPARADOR, ESPACOS_DOIS, TITULO_MENU_REAT_IND

def menu_reatancia_indutiva():
    
    while True:
            print(SEPARADOR)
            print(ESPACOS_DOIS, TITULO_MENU_REAT_IND)
            print(ESPACOS_DOIS, "XL = 2 x π x ƒ x L")
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