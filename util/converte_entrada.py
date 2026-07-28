from util.mensagens import ERRO_ENTRADA_NUMERICA

def converte_entrada(entrada):
    
    if entrada:
        try:
            entrada_convertida = float(entrada)
            return entrada_convertida
        except ValueError:
            raise ValueError(ERRO_ENTRADA_NUMERICA)
    else:
        return None
