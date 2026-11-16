## 7. Documentación (docstring) Crea una función llamada calcular_potencia(base: float, exponente: float) -> float que eleve un número a su potencia.
# Añade un docstring completo que cumpla estrictamente con la advertencia del apunte: 1. Breve explicación. 2. Especificación y tipos de los 
# parámetros. 3. Restricciones (ej. el exponente no debe ser negativo). 4. Características del valor que retorna. 

def calcular_potencia(base: float, exponente: float) -> float:
    """
    Calcula la potencia de un numero.

    Parametros:
        base: numero que se va a elevar.
        exponente: potencia del numero.

    Restricciones:
        El exponente no debe ser negativo.

    Retorna:
        El resultado de la potencia.
    """
    if exponente < 0:
        raise ValueError("El exponente no debe ser negativo")

    return base ** exponente

print(calcular_potencia(2, 3))
