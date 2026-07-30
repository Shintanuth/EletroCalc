from util.constantes import FREQUENCIA_PADRAO
from util.validacoes import validar_maior_que_zero

# ===========================
# Validações Elétrica
# ===========================

def obter_frequencia(frequencia):

    if frequencia is None:
        frequencia = FREQUENCIA_PADRAO

    return frequencia

def validar_quantidade_none(valores, quantidade_none, mensagem):

    if valores.count(None) != quantidade_none:
        raise ValueError(mensagem)

def validar_valores_positivos(valores):

    for valor, mensagem in valores:

        if valor is not None:
            validar_maior_que_zero(valor, mensagem)