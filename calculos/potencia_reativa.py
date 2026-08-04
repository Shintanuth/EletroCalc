from math import sqrt
from util.constantes import VOLT_AMPERE_REATIVO
from util.conversores import (
                              seno_graus, 
                              tangente_graus
                              )
from util.validacoes import (
                             validar_obrigatorio, 
                             validar_obrigatorio_positivo,
                             validar_intervalo,
                             validar_maior
                             )
from util.mensagens import (
                            ERRO_TENSAO_OBRIGATORIA, 
                            ERRO_CORRENTE_OBRIGATORIA,
                            ERRO_ANGULO_OBRIGATORIO,
                            ERRO_ANGULO_POSITIVO,
                            ERRO_TENSAO_POSITIVA,
                            ERRO_CORRENTE_POSITIVA,
                            ERRO_POTENCIA_APARENTE_OBRIGATORIA,
                            ERRO_POTENCIA_ATIVA_OBRIGATORIA,
                            ERRO_POTENCIA_APARENTE_POSITIVA,
                            ERRO_POTENCIA_ATIVA_POSITIVA,
                            ERRO_POTENCIA_ATIVA_MAIOR_QUE_APARENTE
                            )

def calcular_potencia_reativa_por_tensao_corrente_angulo(tensao, corrente, angulo):

    validar_obrigatorio(tensao, ERRO_TENSAO_OBRIGATORIA)
    validar_obrigatorio(corrente, ERRO_CORRENTE_OBRIGATORIA)
    validar_obrigatorio(angulo, ERRO_ANGULO_OBRIGATORIO)

    validar_obrigatorio_positivo([
    (tensao, ERRO_TENSAO_POSITIVA),
    (corrente, ERRO_CORRENTE_POSITIVA),
    (angulo, ERRO_ANGULO_POSITIVO)
    ])

    validar_intervalo(angulo, 0, 90, "O ângulo de defasagem")

    return "Potência Reativa", tensao * corrente * (seno_graus(angulo)), VOLT_AMPERE_REATIVO

def calcular_potencia_reativa_por_potencia_aparente_potencia_ativa(potencia_aparente, potencia_ativa):

    validar_obrigatorio(potencia_aparente, ERRO_POTENCIA_APARENTE_OBRIGATORIA)
    validar_obrigatorio(potencia_ativa, ERRO_POTENCIA_ATIVA_OBRIGATORIA)

    validar_obrigatorio_positivo([
        (potencia_aparente, ERRO_POTENCIA_APARENTE_POSITIVA),
        (potencia_ativa, ERRO_POTENCIA_ATIVA_POSITIVA)
    ])

    validar_maior(potencia_ativa, potencia_aparente, ERRO_POTENCIA_ATIVA_MAIOR_QUE_APARENTE)

    return "Potência Reativa",  sqrt((potencia_aparente**2) - (potencia_ativa**2)) , VOLT_AMPERE_REATIVO

def calcular_potencia_reativa_por_potencia_ativa_angulo(potencia_ativa, angulo):

    validar_obrigatorio(potencia_ativa, ERRO_POTENCIA_ATIVA_OBRIGATORIA)
    validar_obrigatorio(angulo, ERRO_ANGULO_OBRIGATORIO)

    validar_obrigatorio_positivo([
        (potencia_ativa, ERRO_POTENCIA_ATIVA_POSITIVA),
        (angulo, ERRO_ANGULO_POSITIVO)
    ])

    validar_intervalo(angulo, 0, 90, "O ângulo de defasagem")

    return "Potência Reativa", potencia_ativa * (tangente_graus(angulo)), VOLT_AMPERE_REATIVO