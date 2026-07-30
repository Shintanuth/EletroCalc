from util.constantes import WATT, VOLT, AMPERE
from util.mensagens import (
                            ERRO_DOIS_VALORES, 
                            ERRO_CORRENTE_POSITIVA, 
                            ERRO_TENSAO_POSITIVA,
                            ERRO_POTENCIA_POSITIVA
                            )
from util.validacoes_eletricas import (validar_quantidade_none, 
                                       validar_valores_positivos
                                       )

def calcular_potencia_ativa(potencia, tensao, corrente):
    
    valores = [potencia, tensao, corrente]

    validar_quantidade_none(valores, 1, ERRO_DOIS_VALORES)

    validar_valores_positivos([
        (potencia, ERRO_POTENCIA_POSITIVA),
        (tensao, ERRO_TENSAO_POSITIVA),
        (corrente, ERRO_CORRENTE_POSITIVA)
    ])
    
    if potencia is None:    
       
        return "Potência Ativa", tensao * corrente, WATT
        
    if tensao is None:
        
        return "Tensão", potencia / corrente, VOLT
  
    return "Corrente", potencia / tensao, AMPERE

