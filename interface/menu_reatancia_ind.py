from util.sair_do_menu import sair_do_menu
from util.constantes import SEPARADOR

def menu_reatancia_indutiva():
    
    while True:
            print(SEPARADOR)
            print("          Reataância Indutiva ")
            print("           XL = 2 x π x ƒ x L ")
            print(SEPARADOR)
            print("Digite dois valores e deixe um em branco")

            
            print(SEPARADOR)

            opcao = sair_do_menu()
            
            match opcao:
                case "c":
                        continue
                case "v":
                        return
                case "s":
                        return "sair"      