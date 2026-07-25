from util.converte_entrada import converte_entrada
from util.sair_do_menu import sair_do_menu
from calculos.potencia import calcular_potencia
from util.mostrar_resultado import mostrar_resultado
from util.constantes import SEPARADOR, ESPACOS, TITULO_MENU_POTENCIA
from util.mensagens import MSG_DOIS_VALORES

def menu_potencia():
    
    while True:
            print(SEPARADOR)
            print(ESPACOS, TITULO_MENU_POTENCIA)
            print()
            print(ESPACOS, "P = E x I")
            print(ESPACOS, "E = P / I")
            print(ESPACOS, "I = P / E")
            print(SEPARADOR)
            print(MSG_DOIS_VALORES)

            try:
                potencia = converte_entrada(input("Potência (W): "))
                tensao = converte_entrada(input("Tensão (V):"))
                corrente = converte_entrada(input("Corrente (A): "))
                print(SEPARADOR)

                grandeza, resultado, unidade = (calcular_potencia(potencia, tensao, corrente))
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