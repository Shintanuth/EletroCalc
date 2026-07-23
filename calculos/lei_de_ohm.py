def calcular_lei_de_ohm(tensao, corrente, resistencia):
    
    valores = [tensao, corrente, resistencia]

    if valores.count(None) != 1:
        raise ValueError("Digite exatamente dois valores e deixe um em branco para ser calculado.")
    
    if tensao is None:    
       
        resultado = corrente * resistencia
        return "Tensão", resultado, "V"
        
    
    if corrente is None:
        
        if resistencia == 0:
            raise ValueError("A resitência não pode ser zero")

        resultado = tensao / resistencia
        return "Corrente", resultado, "A"
        
        
    
    if resistencia is None:
    
        if corrente == 0:
            raise ValueError("A corrente não pode ser zero")
        
        resultado = tensao / corrente

        return "Resistência", resultado, "Ω"
        
    
    
    