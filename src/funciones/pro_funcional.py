# EJERCICIO PARA MAP
## Recuerde map sirve para transformar todos los elementos
### Ejercicio 1: Tienes una lista de numeros y quieres obtener una nueva lista con el cubo (elevado a 3) de cada numero.

numeros:list[int]=[1,2,3,4]
nueva_lista=list(map(lambda e:e**3,numeros))
print(nueva_lista)

def cubo(e):
    return e**3
map(cubo,numeros)

# EJERCICIO PARA FILTER()
## Ejercicio 2: Tienes una lista de temperaturas (algunas bajo cero).Filtra la lista para quedarte solo con las temperaturas positivas (mayores a 0)

temp:list[int|float]=[-2,10,0,-20,-1,-10,18,23.0]
nueva_temp=list(filter(lambda t:t>0,temp))
print(f"las temperaturas mayores a cero son: {nueva_temp}")

# EJERCICIO COMBINANDO MAP() Y FILTER()
## Tienes una lista de numeros . Primero filtra para quedarte solo con los numeros pares. Luego usa,MAP para multiplicarlos por 10 los numeros pares.
num:list[int]=[2,5,4,8,7]
num_pares=list(filter(lambda n: n % 2 == 0,num))
print(num_pares)
nuevo_lista=list(map(lambda n: n*10,num_pares))

print(nueva_lista)

### REFACTORIZACION: Es una tecnica para mejorar o hacer mas optimo el codigo

num:list[int]=[2,5,4,8,7]
nuevo_lista=list[int]=list(map(lambda n: n*10,filter(lambda n:n % 2 == 0,num)))
print(nueva_lista)

## En una linia de codigo
num:list[int]=[2,5,4,8,7]
print([n*10 for n in num if n%2==0])
