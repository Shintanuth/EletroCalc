from util.constantes import PI, FREQUENCIA_PADRAO, OHM

def calcular_reatancia_capacitiva(frequencia, capacitancia):

    if frequencia is None:
        frequencia = FREQUENCIA_PADRAO

    if frequencia <= 0:
        raise ValueError("A frequência não pode ser 0 e nem negativa")

    if  capacitancia <= 0:
            raise ValueError("O valor da indutância não pode ser 0 e nem negativo")

    if capacitancia is None:
        raise ValueError("O valor da indutância é obrigatório")

    resultado = 2 * PI * frequencia * capacitancia
    return "XC", resultado, OHM
    