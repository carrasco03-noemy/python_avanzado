# FUNCIONES EN PYTHON

- Las funciones nos permite ordenar mejor el codigo y reutilizarlo cuando sea necesario

```python
# EJEMPLO DESEAMOS CREAR UN PROGRAMA EN PYTHON QUE NOS PERMITE SUMAR DOS NUMEROS
numero_uno:int=45
numero_dos:int=70
numero_tres:int=78
numero_cuatro:int=20
suma:int=numero_uno+numero_dos
suma_dos:int=numero_tres+numero_cuatro
print(suma)
print(suma_dos)
```

Como hacemos reutilizable el ejercicio anterior y mas lejible.
para eso utilizaremos FUNCIONES.
La caracteristica de una funcion en python es la siguiente:

1. Debe comenzar con la palabra reservada `def`.

2. Debe tener un nombre que de a entender que realizara la funcion.

3. Debera tener parametros y estos estaran encerrados en parentisis `()`.No todas las funciones resibiran parametros aun asi debera tener los `()`.

4. Las funciones deberan retornar datos a travez de la palabra reservada `return`.

```python
# CREAR UN PROGRAMA QUE ME PERMITA SUMAR DOS NUMEROS

def sumar(a:int,b:int):
    return a+b

print(sumar(78,56))
print(sumar(45,5))
```
