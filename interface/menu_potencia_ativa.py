from util.mensagens import MSG_OPCAO, ERRO_OPCAO_INVALIDA, MSG_EM_DESENVOLVIMENTO
from util.constantes import (
                             TITULO_MENU_POTENCIA,
                             OPCOES_MENU_POTENCIA_ATIVA,
                             SELETOR_MENU_POTENCIA_ATIVA
                             )
from util.interface import (
                            mostrar_cabecalho, 
                            mostrar_opcoes,
                            mostrar_erro,
                            mostrar_aviso
                            )
from util.validacoes import validar_opcao
from interface.menu_potencia_ativa_tensao_corrente_fator_de_potencia import menu_potencia_ativa_tensao_corrente_fator_de_potencia
from interface.menu_potencia_ativa_potencia_aparente_fator_de_potencia import menu_potencia_ativa_potencia_aparente_fator_de_potencia
def menu_potencia_ativa():
    
    while True:
    
            mostrar_cabecalho(TITULO_MENU_POTENCIA)
    
            opcao = mostrar_opcoes(OPCOES_MENU_POTENCIA_ATIVA)
    
    
            try:
    
                opcao = input(MSG_OPCAO)
    
                validar_opcao(opcao, SELETOR_MENU_POTENCIA_ATIVA, ERRO_OPCAO_INVALIDA)
    
            except ValueError as erro:
                mostrar_erro(erro)
                continue
    
            match opcao:
                        case "1":
                             menu_potencia_ativa_tensao_corrente_fator_de_potencia()
                        case "2":
                             menu_potencia_ativa_potencia_aparente_fator_de_potencia()
                             continue
                        case "3":
                             mostrar_aviso(MSG_EM_DESENVOLVIMENTO)
                             continue
                        case "c":
                            continue
                        case "v":
                            return
                        case "s":
                            return "sair"