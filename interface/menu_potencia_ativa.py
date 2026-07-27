from util.converte_entrada import converte_entrada
from util.sair_do_menu import sair_do_menu
from calculos.potencia import calcular_potencia_ativa
from util.constantes import SEPARADOR, ESPACOS, TITULO_MENU_POTENCIA,FORMULA_POTENCIA_ATIVA
from util.mensagens import MSG_DOIS_VALORES
from util.interface import mostrar_cabecalho, mostrar_resultado

def menu_potencia_ativa():
    
    while True:
           
            mostrar_cabecalho(TITULO_MENU_POTENCIA, FORMULA_POTENCIA_ATIVA)

            print(SEPARADOR)
            print(MSG_DOIS_VALORES)
            print(SEPARADOR)

            try:
                potencia = converte_entrada(input("Potência (W): "))
                tensao = converte_entrada(input("Tensão (V):"))
                corrente = converte_entrada(input("Corrente (A): "))
                print(SEPARADOR)

                grandeza, resultado, unidade = (calcular_potencia_ativa(potencia, tensao, corrente))
                print(mostrar_resultado(grandeza, resultado, unidade))
                         
            except ValueError as erro:
                 print(erro)
                 continue             
             

            opcao = sair_do_menu()
           
            match opcao:
                case "c":
                        continue
                case "v":
                        return
                case "s":
                        return "sair"      