from util.validacoes_eletricas import validar_valores_positivos
from util.validacoes import validar_obrigatorio, validar_intervalo
from util.constantes import WATT
from util.mensagens import (
                            ERRO_TENSAO_POSITIVA, 
                            ERRO_CORRENTE_POSITIVA, 
                            ERRO_TENSAO_OBRIGATORIA, 
                            ERRO_CORRENTE_OBRIGATORIA,
                            ERRO_POTENCIA_APARENTE_POSITIVA,
                            ERRO_POTENCIA_APARENTE_OBRIGATORIA,
                            ERRO_POTENCIA_REATIVA_OBRIGATORIA,
                            ERRO_FATOR_DE_POTENCIA_OBRIGATORIO,
                            ERRO_FATOR_DE_POTENCIA_POSITIVO
                            )
from math import sqrt

def calcular_potencia_ativa_tensao_corrente_fator_de_potencia(tensao, corrente, fator_de_potencia):

    validar_obrigatorio(tensao, ERRO_TENSAO_OBRIGATORIA)
    validar_obrigatorio(corrente, ERRO_CORRENTE_OBRIGATORIA)
    validar_obrigatorio(fator_de_potencia,ERRO_FATOR_DE_POTENCIA_OBRIGATORIO)

    validar_valores_positivos([
        (tensao, ERRO_TENSAO_POSITIVA),
        (corrente, ERRO_CORRENTE_POSITIVA),
        (fator_de_potencia, ERRO_FATOR_DE_POTENCIA_POSITIVO)
    ])

    validar_intervalo(fator_de_potencia, 0, 1, "O fator de potência")

    return "Potência Ativa", tensao * corrente * fator_de_potencia, WATT

def calcular_potencia_ativa_potencia_aparente_fator_de_potencia(potencia_aparente, fator_de_potencia):

    validar_obrigatorio(potencia_aparente, ERRO_POTENCIA_APARENTE_OBRIGATORIA)
    validar_obrigatorio(fator_de_potencia, ERRO_FATOR_DE_POTENCIA_OBRIGATORIO)

    validar_valores_positivos([
        (potencia_aparente, ERRO_POTENCIA_APARENTE_POSITIVA),
        (fator_de_potencia, ERRO_FATOR_DE_POTENCIA_POSITIVO)
    ])

    validar_intervalo(fator_de_potencia, 0, 1, "O fator de potência")

    return "Potência Ativa", potencia_aparente * fator_de_potencia, WATT

def calcular_potencia_ativa_potencia_aparente_potencia_reativa(potencia_aparente, potencia_reativa):

    validar_obrigatorio(potencia_aparente, ERRO_POTENCIA_APARENTE_OBRIGATORIA)
    validar_obrigatorio(potencia_reativa, ERRO_POTENCIA_REATIVA_OBRIGATORIA)

    validar_valores_positivos([
        (potencia_aparente, ERRO_POTENCIA_APARENTE_POSITIVA)
    ])

    return "Potência Ativa",  sqrt((potencia_aparente**2) - (potencia_reativa**2)), WATT
