from util.constantes import PI, OHM
from util.conversores import uf_para_f
from util.mensagens import(
                           ERRO_FREQUENCIA_POSITIVA, 
                           ERRO_CAPACITANCIA_OBRIGATORIA, 
                           ERRO_CAPACITANCIA_POSITIVA
                           )
from util.validacoes_eletricas import (
                                       validar_valores_positivos, 
                                       obter_frequencia
                                       )

def calcular_reatancia_capacitiva(frequencia, capacitancia):

    frequencia = obter_frequencia(frequencia)

    validar_valores_positivos([
          (frequencia, ERRO_FREQUENCIA_POSITIVA),
          (capacitancia, ERRO_CAPACITANCIA_POSITIVA)
    ])

    if capacitancia is None:
            raise ValueError(ERRO_CAPACITANCIA_OBRIGATORIA)
    
    capacitancia = uf_para_f(capacitancia)
    resultado = 1 / (2 * PI * frequencia * capacitancia)
    return "XC", resultado, OHM
    