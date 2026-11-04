# Ejercicio usando la tecnica *args crear una funcion que me permita identificar numeros pares de n cantidad 
# de numeros pasados por argumento la funcion debera retornar una lista con los numeros pares identificados

def num_pares (*args)->list[int]:
    pares:list[int]=[]
    for i in args:
        if i % 2 == 0:
            pares.append(i)
    return pares
print(num_pares(2,4,10,12,7,11,3,9))