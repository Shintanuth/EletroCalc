from util.sair_do_menu import sair_do_menu

def menu_reatancia_indutiva():
    
    while True:
            print("========================================")
            print("          Reataância Indutiva ")
            print("           XL = 2 x π x ƒ x L ")
            print("========================================")
            print("Digite dois valores e deixe um em branco")

            ...

            opcao = sair_do_menu()
            
            match opcao:
                case "c":
                        continue
                case "v":
                        return
                case "s":
                        return "sair"      