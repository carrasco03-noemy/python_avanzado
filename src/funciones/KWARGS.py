# Crear una funcion que me permita saber una lista de ingredientes cual es el de mayor precio
# EJEMPLO
# entrada:ajo=2,papa=3,aceite=8
# salida: el ingrediente de mayor precio es aceite

def ingredientes(**kwargs):
    # **kwargs={'ajo'=2,'papa'=3,'aceite'=8}
    precio_maximo = 0
    ingrediente_mayor = 0
    for ingredientes,precio in kwargs.items():
        if precio > precio_maximo:
            precio_maximo = precio
            ingrediente_mayor = ingredientes
    return ingrediente_mayor
print(ingredientes(ajo=2,papa=3,aceite=8))

## CON MAS INGRDIENTES
def ingredientes(**kwargs):
    # **kwargs={'ajo'=2,'papa'=3,'aceite'=8,'lechuga'=10,'camote'=1}
    precio_maximo = 0
    ingrediente_mayor = 0
    for ingredientes,precio in kwargs.items():
        if precio > precio_maximo:
            precio_maximo = precio
            ingrediente_mayor = ingredientes
    return ingrediente_mayor
print(ingredientes(ajo=2,papa=3,aceite=8,lechuga=10,camote=1))


