from util.sair_do_menu import sair_do_menu

def menu_reatancia_capacitiva():
    
    while True:
            print("================================")
            print("     Reatância Capacitiva")
            print("     Xc = 1 / 2 π x ƒ x C")
            print("================================")



            opcao = sair_do_menu()
            
            match opcao:
                case "c":
                        continue
                case "v":
                        return
                case "s":
                        return "sair"   