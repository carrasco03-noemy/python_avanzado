# CREAR UN PROGRAMA QUE ME PERMITA DESARROLLAR LAS 4 OPERACIONES BASICAS
#  (SUMA,RESTA,DIVICION,MULTIPLICACION)

def suma(a:int,b:int):
    return a+b

def resta(a:int,b:int):
    return a-b

def multiplicacion(a,b):
    return a*b

def divicion(a:int,b:int):
    return a/b

print("suma:",suma(10,11))
print("resta:",resta(7,6))
print("multiplicacion:",multiplicacion(4,3))
print("divicion:",divicion(16,5))


def operaciones(n:list,o:str):
    if o=="+":
        return sum(n)
print(operaciones([4,8,3.2],"+"))
