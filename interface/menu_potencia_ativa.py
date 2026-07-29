from calculos.potencia import calcular_potencia_ativa
from util.constantes import SEPARADOR, TITULO_MENU_POTENCIA,FORMULA_POTENCIA_ATIVA, WATT, VOLT, AMPERE
from util.mensagens import MSG_DOIS_VALORES
from util.interface import mostrar_cabecalho, mostrar_resultado, mostrar_erro, ler_entrada, sair_do_menu

def menu_potencia_ativa():
    
    while True:
           
            mostrar_cabecalho(TITULO_MENU_POTENCIA, FORMULA_POTENCIA_ATIVA)

            print(SEPARADOR)
            print(MSG_DOIS_VALORES)
            print(SEPARADOR)

            try:
                potencia = ler_entrada("Potência", WATT)
                tensao = ler_entrada("Tensão", VOLT)
                corrente = ler_entrada("Corrente", AMPERE)

                print(SEPARADOR)

                grandeza, resultado, unidade = (calcular_potencia_ativa(potencia, tensao, corrente))
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