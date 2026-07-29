from util.constantes import PI, FREQUENCIA_PADRAO, OHM
from util.converte_unidades import mh_para_h
from util.mensagens import (
                            ERRO_FREQUENCIA_POSITIVA, 
                            ERRO_INDUTANCIA_OBRIGATORIA, 
                            ERRO_INDUTANCIA_POSITIVA
                            )

def calcular_reatancia_indutiva(frequencia, indutancia):

    if frequencia is None:
        frequencia = FREQUENCIA_PADRAO

    if frequencia <= 0:
        raise ValueError(ERRO_FREQUENCIA_POSITIVA)

    if indutancia is None:
        raise ValueError(ERRO_INDUTANCIA_OBRIGATORIA)

    if indutancia <= 0:
        raise ValueError(ERRO_INDUTANCIA_POSITIVA)

    indutancia = mh_para_h(indutancia)
    resultado = 2 * PI * frequencia * indutancia
    return "XL", resultado, OHM
    
