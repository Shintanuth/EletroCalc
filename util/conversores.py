from util.mensagens import ERRO_ENTRADA_NUMERICA

# ===========================
# Conversoeres 
# ===========================

def converte_entrada(entrada):
    
    if entrada:
        try:
            entrada_convertida = float(entrada)
            return entrada_convertida
        except ValueError:
            raise ValueError(ERRO_ENTRADA_NUMERICA)
    else:
        return None

# ===========================
# Conversores de unidades
# ===========================

def mh_para_h(valor):
    return valor / 1_000

def uf_para_f(valor):
    return valor / 1_000_000