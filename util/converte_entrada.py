def converte_entrada(entrada):
    
    if entrada:
        try:
            entrada_convertida = float(entrada)
            return entrada_convertida
        except ValueError:
            raise ValueError("Digite um número")
    else:
        return None
