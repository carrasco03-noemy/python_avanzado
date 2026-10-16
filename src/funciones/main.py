# CREAR UN PROGRAMA QUE ME PERMITA MOSTRAR  MENSAJES PERSOONALIZADOS,
# CREAR UNA FUNCION SIMILAR A LA FUNCION PRINT DE PYTHON
def mi_print(mensaje:str):
    texto=f"""
    ---------------------------------
    {mensaje}
    ---------------------------------
    """
    print(texto)

mi_print("BIENVENIDO")
mi_print("HOLA BUENOS DIAS")

# PRIMER EJEMPLO
def contar(n):
    if n == 0:
        print(0)
    else:
        print(n)
        contar(n - 1)

contar(5)

# SEGUNDO EJEMPLO
def sumar(n):
    if n == 0:
        return 0
    else:
        return n + sumar(n - 1)

print(sumar(5))