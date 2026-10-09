## CREAR UNA FUNCION QUE RECIBA 5 NUMEROS ENTEROS Y QUE RETORNE SOLO UNA LISTA DE
#  NUMEROS DE NUMEROS PARES ,TENER ENCUENTA LAS ANOTACIONES

def numeros_lista (a:int,b:int,c:int,d:int,e:int)->list[int]:
    lista=[a,b,c,d,e]
    return [n for n in lista if n % 2 == 0]
print(numeros_lista(2,5,8,3,10))
