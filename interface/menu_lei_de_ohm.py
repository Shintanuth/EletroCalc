from calculos.lei_de_ohm import calcular_lei_de_ohm
from util.constantes import SEPARADOR, TITULO_MENU_LEI_DE_OHM, FORMULA_LEI_DE_OHM, VOLT, AMPERE, OHM
from util.mensagens import MSG_DOIS_VALORES
from util.interface import mostrar_cabecalho, mostrar_resultado, mostrar_erro, ler_entrada, sair_do_menu

def menu_lei_de_ohm():
    while True:
           
            mostrar_cabecalho(TITULO_MENU_LEI_DE_OHM, FORMULA_LEI_DE_OHM )

            print(SEPARADOR)
            print(MSG_DOIS_VALORES)
            print(SEPARADOR)

            try:
                tensao = ler_entrada("Tensão", VOLT)
                corrente = ler_entrada("Corrente", AMPERE)
                resistencia = ler_entrada("Resistência", OHM)
                print(SEPARADOR)

                grandeza, resultado, unidade = (calcular_lei_de_ohm(tensao, corrente, resistencia))
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
                 
           
                    


                    