from util.constantes import WATT, VOLT, AMPERE

def calcular_potencia(potencia, tensao, corrente):
    
    valores = [potencia, tensao, corrente]

    if valores.count(None) != 1:
        raise ValueError("Digite ESTRITAMENTE dois valores.")
    
    if potencia is None:    
       
        resultado = tensao * corrente
        return "Potência", resultado, WATT
        
    
    if tensao is None:
        
        if corrente == 0:
            raise ValueError("A resistência não pode ser zero")

        resultado = potencia / corrente
        return "Tensão", resultado, VOLT
        
        
    
    if corrente is None:
    
        if tensao == 0:
            raise ValueError("A corrente não pode ser zero")
        
        resultado = potencia / tensao

        return "Corrente", resultado, AMPERE