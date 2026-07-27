from util.sair_do_menu import sair_do_menu
from util.constantes import SEPARADOR, TITULO_MENU_REAT_CAP, FORMULA_REATANCIA_CAPACITIVA, HERTZ, FARAD 
from util.interface import mostrar_resultado, mostrar_cabecalho, mostrar_erro, ler_entrada
from calculos.reatancia_cap import calcular_reatancia_capacitiva

def menu_reatancia_capacitiva():
    
    while True:
            
            mostrar_cabecalho(TITULO_MENU_REAT_CAP, FORMULA_REATANCIA_CAPACITIVA)

            print(SEPARADOR)

            try:
                frequencia = ler_entrada("Frequência", HERTZ)
                capacitancia = ler_entrada("Capacitância", FARAD)

                print(SEPARADOR)
            
                grandeza, resultado, unidade = (calcular_reatancia_capacitiva(frequencia, capacitancia))
                print(mostrar_resultado(grandeza, resultado, unidade))
            
            except ValueError as erro:
                mostrar_erro(erro)    
                continue

            opcao = sair_do_menu()
            
            match opcao:
                case "c":
                        continue
                case "v":
                        return
                case "s":
                        return "sair"   