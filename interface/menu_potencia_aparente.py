from util.constantes import (
                             TITULO_MENU_POTENCIA_APARENTE, 
                             OPCOES_MENU_POTENCIA_APARENTE, 
                             SELETOR_MENU_POTENCIA_APARENTE
                             )
from util.mensagens import (
                            MSG_OPCAO,  
                            ERRO_OPCAO_INVALIDA,
                            MSG_EM_DESENVOLVIMENTO
                            )
from util.validacoes import validar_opcao
from util.interface import (
                            mostrar_cabecalho, 
                            mostrar_opcoes, 
                            mostrar_erro,
                            mostrar_aviso,
                            formatar_texto,
                            )
from interface.menu_potencia_aparente_tensao_corrente import menu_potencia_aparente_tensao_corrente
from calculos.potencia_aparente import calcular_potencia_aparente_por_tensao_e_corrente

def menu_potencia_aparente():

    while True:

        mostrar_cabecalho(TITULO_MENU_POTENCIA_APARENTE)

        opcao = mostrar_opcoes(OPCOES_MENU_POTENCIA_APARENTE)


        try:

            opcao = input(MSG_OPCAO)

            validar_opcao(opcao, SELETOR_MENU_POTENCIA_APARENTE, ERRO_OPCAO_INVALIDA)

        except ValueError as erro:
            mostrar_erro(erro)
            continue

        match opcao:
                    case "1":
                         menu_potencia_aparente_tensao_corrente()
                    case "2":
                         print(mostrar_aviso(formatar_texto(MSG_EM_DESENVOLVIMENTO)))
                         continue
                    case "3":
                         print(mostrar_aviso(formatar_texto(MSG_EM_DESENVOLVIMENTO)))
                         continue
                    case "c":
                        continue
                    case "v":
                        return
                    case "s":
                        return "sair"