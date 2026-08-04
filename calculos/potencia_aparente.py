from math import sqrt

from util.constantes import VOLT_AMPERE
from util.mensagens import (
    ERRO_CORRENTE_OBRIGATORIA,
    ERRO_CORRENTE_POSITIVA,
    ERRO_FATOR_DE_POTENCIA_OBRIGATORIO,
    ERRO_POTENCIA_ATIVA_OBRIGATORIA,
    ERRO_POTENCIA_ATIVA_POSITIVA,
    ERRO_POTENCIA_REATIVA_OBRIGATORIA,
    ERRO_TENSAO_OBRIGATORIA,
    ERRO_TENSAO_POSITIVA,
)
from util.validacoes import validar_intervalo, validar_obrigatorio
from util.validacoes_eletricas import validar_valores_positivos


def calcular_potencia_aparente_por_tensao_e_corrente(tensao, corrente):

    validar_obrigatorio(tensao, ERRO_TENSAO_OBRIGATORIA)

    validar_obrigatorio(corrente, ERRO_CORRENTE_OBRIGATORIA)

    validar_valores_positivos(
        [(tensao, ERRO_TENSAO_POSITIVA), (corrente, ERRO_CORRENTE_POSITIVA)]
    )

    return "Potência Aparente", tensao * corrente, VOLT_AMPERE


def calcular_potencia_aparente_por_potencia_ativa_e_fator_de_potencia(
    potencia_ativa, fator_de_potencia
):

    validar_obrigatorio(potencia_ativa, ERRO_POTENCIA_ATIVA_OBRIGATORIA)

    validar_obrigatorio(fator_de_potencia, ERRO_FATOR_DE_POTENCIA_OBRIGATORIO)

    validar_valores_positivos(
        [
            (potencia_ativa, ERRO_POTENCIA_ATIVA_POSITIVA),
        ]
    )

    validar_intervalo(fator_de_potencia, 0, 1, "O fator de potência")

    return "Potência Aparente", potencia_ativa / fator_de_potencia, VOLT_AMPERE


def calcular_potencia_aparente_por_potencia_ativa_e_potencia_reativa(
    potencia_ativa, potencia_reativa
):

    validar_obrigatorio(potencia_ativa, ERRO_POTENCIA_ATIVA_OBRIGATORIA)

    validar_obrigatorio(potencia_reativa, ERRO_POTENCIA_REATIVA_OBRIGATORIA)

    validar_valores_positivos(
        [
            (potencia_ativa, ERRO_POTENCIA_ATIVA_POSITIVA),
        ]
    )

    return (
        "Potência Aparente",
        sqrt((potencia_ativa**2) + (potencia_reativa**2)),
        VOLT_AMPERE,
    )
