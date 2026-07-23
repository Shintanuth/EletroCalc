def mostrar_resultado_lei_de_ohm(valor, resultado):

    if valor == "tensao":
        return f'Tensão = {resultado}'

    if valor == "corrente":
        return f'Corrente = {resultado}'

    if valor == "resistencia":
        return f'Resistência = {resultado}'