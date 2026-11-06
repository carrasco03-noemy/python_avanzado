# En  la siguiente funcion deberan escribir la documentacion segun la convencion para el docstring de funciones.
def area_rectangulo(b,h):
    """ 
    calcular el area de un rectangulo
    Args:
     b= base (int|float) este argumento sera la base del rectangulo
     h= altura (int|float) este argumento sera la altura del rectangulo
    Raises:
       los argumentos no podran ser iguales o menores a 0.
    Returns:
       int|float:el resultado del la operacion b*h (base*altura)
    """
    return b*h

# Funcion para hallar la potencia de un numero

def potencia (n:int,p:int)-> int:
    resultado:int=1
    for _ in range(p):
        resultado *= n
    """calcular la potencia
    Args:
     n=numero(int) sera el numero que se multiplicara
     p=potencia(int) sera la cantidad de veses que se va multiplicar
    Returns:
        int : resultado de la cantidad que se multiplico el numero
    """
    return resultado

