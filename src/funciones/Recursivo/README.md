# **RECURSIVIDAD EN PYTHON**

Es una técnica de programación en la que una función se llama a sí misma para resolver un problema. Se utiliza para dividir un problema en partes más pequeñas hasta llegar a una condición que permita detenerse.

# *COMO FUNCIONA*

1. La función comienza
Recibe un dato, por ejemplo, el número 3.

2. Se llama a sí misma
Resuelve el problema con un número menor: 3, 2, 1...

3. Llega al caso base
Al llegar a 0, deja de llamarse.

4. Devuelve el resultado
Las llamadas anteriores terminan de resolver el problema.

# EJEMPLOS

Ejemplo  01 :CONTAR NUMEROS

```python
def contar(n):
    if n == 0:
        print(0)
    else:
        print(n)
        contar(n - 1)

contar(5)
```

RESULTADO:
5
4
3
2
1
0

Explicación: la función contar`()` se llama a sí misma restando uno al número. Cuando llega a cero, se detiene.

Ejemplo 02: SUMAR NUEMROS

```python
def sumar(n):
    if n == 0:
        return 0
    else:
        return n + sumar(n - 1)

print(sumar(5))
```

RESULTADO:
15

# ¿PARA QUE SIRVE LA RECURSIVIDAD?

La recursividad sirve para resolver problemas que pueden dividirse en partes más pequeñas. Se puede utilizar en diferentes áreas de la programación.