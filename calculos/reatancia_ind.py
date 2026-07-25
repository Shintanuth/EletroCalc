from util.constantes import PI, FREQUENCIA_PADRAO, OHM

def calcular_reatancia_indutiva(frequencia, indutancia):

    if frequencia is None:
        frequencia = FREQUENCIA_PADRAO

    if frequencia <= 0:
        raise ValueError("A frequência não pode ser 0 e nem negativa")

    if indutancia <= 0:
            raise ValueError("O valor da indutância não pode ser 0 e nem negativo")

    if indutancia is None:
        raise ValueError("O valor da indutância é obrigatório")

    indutancia = indutancia / 1000
    resultado = 2 * PI * frequencia * indutancia
    return "XL", resultado, OHM
    
