## CREAR UNA FUNCION QUE RECIBA 5 NUMEROS ENTEROS Y QUE RETORNE SOLO UNA LISTA DE
#  NUMEROS DE NUMEROS PARES ,TENER ENCUENTA LAS ANOTACIONES

def num_pares (a:int,b:int,c:int,d:int,e:int)->list[int]:
    numeros:list[int]=[a,b,c,d,e]
    numeros_pares:list[int]=[]
    for i in numeros:
        if i % 2 == 0:
            numeros_pares.append(i)
    return numeros_pares
# print(num_pares(4,2,5,7,8))

# EJEMPLOS DE POCICION NOMINAL
def suma(a:int,b:int)->int:
    return a+b
print(suma(34+45))

#EJEMPLO DE LOGIN
def login(user="",password=""):
    return "bienvenido al sistema"
print(login(user="hola"))


