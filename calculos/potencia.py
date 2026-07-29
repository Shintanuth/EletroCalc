from util.constantes import WATT, VOLT, AMPERE
from util.mensagens import (
                            ERRO_DOIS_VALORES, 
                            ERRO_CORRENTE_POSITIVA, 
                            ERRO_TENSAO_POSITIVA
                            )

def calcular_potencia_ativa(potencia, tensao, corrente):
    
    valores = [potencia, tensao, corrente]

    if valores.count(None) != 1:
        raise ValueError(ERRO_DOIS_VALORES)
    
    if potencia is None:    
       
        resultado = tensao * corrente
        return "Potência Ativa", resultado, WATT
        
    if tensao is None:
        
        if corrente == 0:
            raise ValueError(ERRO_CORRENTE_POSITIVA)

        resultado = potencia / corrente
        return "Tensão", resultado, VOLT
        
    if corrente is None:
    
        if tensao == 0:
            raise ValueError(ERRO_TENSAO_POSITIVA)
        
        resultado = potencia / tensao

        return "Corrente", resultado, AMPERE