def dividir(dividendo, divisor):
    """
    Divide dos números no negativos.
    
    Args:
        dividendo: El número a ser dividido
        divisor: El número por el cual se divide
        
    Returns:
        El resultado de la división (resultado entero)
        
    Raises:
        Exception: Si alguno de los números es negativo
        Exception: Si el divisor es cero
    """
    # Validar que ambos números sean no negativos
    if dividendo < 0 or divisor < 0:
        raise Exception("Los numeros deben ser positivos")
    
    # Validar que no haya división por cero
    if divisor == 0:
        raise Exception("No se puede dividir por cero")
    
    # Realizar la división entera
    return dividendo // divisor
