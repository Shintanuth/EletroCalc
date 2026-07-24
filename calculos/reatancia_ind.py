from util.constantes import PI

def calcular_reatancia_indutiva(frequencia, indutancia):


    if frequencia != None:

        if indutancia != None:
            resultado = 2 * PI * frequencia * indutancia
            return "Indutância", resultado, "H"

        raise ValueError("Informe o valor da indutância")

    resultado = 2 * PI * 60 * indutancia
    return "Indutância", resultado, "H"