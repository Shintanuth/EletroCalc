from util.constantes import OHM, AMPERE, VOLT
from util.mensagens import (
                            ERRO_DOIS_VALORES, 
                            ERRO_CORRENTE_POSITIVA, 
                            ERRO_RESISTENCIA_POSITIVA,
                            ERRO_TENSAO_POSITIVA
                            )
from util.validacoes_eletricas import validar_quantidade_none, validar_valores_positivos

def calcular_lei_de_ohm(tensao, corrente, resistencia):
    
    valores = [tensao, corrente, resistencia]

    validar_quantidade_none(valores, 1, ERRO_DOIS_VALORES)

    validar_valores_positivos([
        (tensao, ERRO_TENSAO_POSITIVA),
        (corrente, ERRO_CORRENTE_POSITIVA),
        (resistencia, ERRO_RESISTENCIA_POSITIVA)
    ])
    
    if tensao is None:
        return "Tensão", corrente * resistencia, VOLT

    if corrente is None:
        return "Corrente", tensao / resistencia, AMPERE

    return "Resistência", tensao / corrente, OHM
        
    
    
    