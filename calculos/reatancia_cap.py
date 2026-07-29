from util.constantes import PI, FREQUENCIA_PADRAO, OHM
from util.converte_unidades import uf_para_f
from util.mensagens import(
                           ERRO_FREQUENCIA_POSITIVA, 
                           ERRO_CAPACITANCIA_OBRIGATORIA, 
                           ERRO_CAPACITANCIA_POSITIVA
                           )

def calcular_reatancia_capacitiva(frequencia, capacitancia):

    if frequencia is None:
        frequencia = FREQUENCIA_PADRAO

    if frequencia <= 0:
        raise ValueError(ERRO_FREQUENCIA_POSITIVA)

    if capacitancia is None:
            raise ValueError(ERRO_CAPACITANCIA_OBRIGATORIA)

    if  capacitancia <= 0:
            raise ValueError(ERRO_CAPACITANCIA_POSITIVA)
    
    capacitancia = uf_para_f(capacitancia)
    resultado = 1 / (2 * PI * frequencia * capacitancia)
    return "XC", resultado, OHM
    