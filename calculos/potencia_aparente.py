from util.validacoes_eletricas import validar_valores_positivos
from util.validacoes import validar_obrigatorio
from util.mensagens import (
                            ERRO_TENSAO_POSITIVA, 
                            ERRO_CORRENTE_POSITIVA, 
                            ERRO_TENSAO_OBRIGATORIA, 
                            ERRO_CORRENTE_OBRIGATORIA
                            )
from math import sqrt

def calcular_potencia_aparente_por_tensao_e_corrente(tensao, corrente):

    validar_obrigatorio(tensao, ERRO_TENSAO_OBRIGATORIA)

    validar_obrigatorio(corrente, ERRO_CORRENTE_OBRIGATORIA)

    validar_valores_positivos([
            (tensao, ERRO_TENSAO_POSITIVA),
            (corrente, ERRO_CORRENTE_POSITIVA)
        ])
 
    return tensao * corrente

def calcular_potencia_aparente_por_potencia_ativa_e_fator_de_potencia(potencia_ativa, fator_de_potencia):

    return potencia_ativa / fator_de_potencia

def calcular_potencia_aparente_por_potencia_ativa_e_potencia_reativa(potencia_ativa, potencia_reativa):

    return sqrt((potencia_ativa**2) + (potencia_reativa**2))