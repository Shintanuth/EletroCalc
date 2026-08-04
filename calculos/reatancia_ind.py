from util.constantes import OHM, PI
from util.conversores import mh_para_h
from util.mensagens import (
    ERRO_FREQUENCIA_POSITIVA,
    ERRO_INDUTANCIA_OBRIGATORIA,
    ERRO_INDUTANCIA_POSITIVA,
)
from util.validacoes_eletricas import obter_frequencia, validar_valores_positivos


def calcular_reatancia_indutiva(frequencia, indutancia):

    frequencia = obter_frequencia(frequencia)

    validar_valores_positivos(
        [(frequencia, ERRO_FREQUENCIA_POSITIVA), (indutancia, ERRO_INDUTANCIA_POSITIVA)]
    )

    if indutancia is None:
        raise ValueError(ERRO_INDUTANCIA_OBRIGATORIA)

    indutancia = mh_para_h(indutancia)
    resultado = 2 * PI * frequencia * indutancia
    return "XL", resultado, OHM
