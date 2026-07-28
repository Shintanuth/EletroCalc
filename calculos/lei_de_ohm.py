from util.constantes import OHM, AMPERE, VOLT
from util.mensagens import ERRO_DOIS_VALORES, ERRO_CORRENTE_POSITIVA, ERRO_RESISTENCIA_POSITIVA

def calcular_lei_de_ohm(tensao, corrente, resistencia):
    
    valores = [tensao, corrente, resistencia]

    if valores.count(None) != 1:
        raise ValueError(ERRO_DOIS_VALORES)
    
    if tensao is None:    
       
        resultado = corrente * resistencia
        return "Tensão", resultado, VOLT
        
    
    if corrente is None:
        
        if resistencia == 0:
            raise ValueError(ERRO_RESISTENCIA_POSITIVA)

        resultado = tensao / resistencia
        return "Corrente", resultado, AMPERE
        
        
    
    if resistencia is None:
    
        if corrente == 0:
            raise ValueError(ERRO_CORRENTE_POSITIVA)
        
        resultado = tensao / corrente

        return "Resistência", resultado, OHM
        
    
    
    