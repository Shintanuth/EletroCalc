from util.constantes import OHM, PI
from util.conversores import uf_para_f
from util.mensagens import (
    ERRO_CAPACITANCIA_OBRIGATORIA,
    ERRO_CAPACITANCIA_POSITIVA,
    ERRO_FREQUENCIA_POSITIVA,
)
from util.validacoes_eletricas import obter_frequencia, validar_valores_positivos


def calcular_reatancia_capacitiva(frequencia, capacitancia):

    frequencia = obter_frequencia(frequencia)

    validar_valores_positivos(
        [
            (frequencia, ERRO_FREQUENCIA_POSITIVA),
            (capacitancia, ERRO_CAPACITANCIA_POSITIVA),
        ]
    )

    if capacitancia is None:
        raise ValueError(ERRO_CAPACITANCIA_OBRIGATORIA)

    capacitancia = uf_para_f(capacitancia)
    resultado = 1 / (2 * PI * frequencia * capacitancia)
    return "XC", resultado, OHM
