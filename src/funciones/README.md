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

## FUNCIONES AVANZADAS

Existen tres grandes conceptos para poder entender el uso avanzada de las funciones:

1. Argumentos,parametros posicionales,nominales,*args y +kargs.

2. Anotaciones en la salida de una funcion.

3. Recursividad.

------------------------------------------------------------------------------------

```python
# ANOTACIONES EN UNA FUNCION

def suma(a:int,b:float)->int:
    return a+b
```

- CREAR SOLO LAS ANOTACIONES DE UNA FUNCION QUE RESIVA CUANTRO NUMEROS ENTEROS Y COMO SALIDA QUE ME MUESTRE 4 NUMEROS ENTEROS EN UNA LISTA

```python
 def numeros_lista (a:int,b:int,c:int,d:int)->list[int]:
    return [a,b,c,d]
```

------------------------------------------------------------------------------------

**ARGUMENTOS PARAMETROS**

```python
 def numeros_lista (a:int,b:int,c:int,d:int)->list[int]:
    return [a,b,c,d]
```

- **PARAMETROS** - Los parametros son las variables que se declaran en la definicion de la funcion.
- **ARGUMENTOS** - Es el dato concreto enviado en el llamado de la funcion.

**NOTA** En ambos casos tenemos los *pocicionales/nominales*.

```python
# PARAMETROS
 def suma(a,b) -> # En este caso tenemos una funcion suma que recibe dos parametros a,b.

suma(34,45) -> # En este caso estoy llamando a la funcion pasandole como argumento los datos.

# En este caso en concreto podemos decir que estamos frente a una funcion que tiene parametros posicionales,eso significa que cada valor reemplaza en el orden que le pasemos a las variables, 34 -> a, 45 -> b.

def login(usuario="",password=""):
    return "acceso correcto"
login(password="12345678",usuario="tupapi") -> # Esta funcion es nominal por que para pasar los valores tengo que indicar la variable a la que le va asociar en el parametro de la funcion.
```

## CONOCIENDO MAS SOBRE FUNCIONES **PARAMETROS Y ARGUMENTOS**

Sobre los parametros/argumentos nominales es ampliamente usado para distintas configuraciones ya que se puede pasar argumentos solo los argumentos que se usaran y dejar los parametros por defecto si no se van a modificar.

```python
# Tenemos un programa que me permite acceder a internet que tiene parametros por defecto sin embargo si se actualiza uno de los accesos se podra modificar el valor.

## PRIMER CASO ACCESOS POR DEFECTO
def config (user="admin",pass="1234",port="8080",BSSID="WIFI"):
    return "conectado a la red"
config()

## SEGUNDO CASO 1 BSSID CAMBIO POR EL DE "LANORATORIO1"
def config (user="admin",pass="1234",port="8080",BSSID="WIFI"):
    return "conectado a la red"
config(BSSID="laboratorio1")

## REYNER DESEA CONECTARSE AL WIFI DE ANA LUZ,PREGUNTA COMO SE LLAMA TU WIFI Y CUAL ES LA CONTRASEÑA.RESPUESTA LE DISE EL WIFI ES A56 Y SU CONTRASEÑA ES 12345678
def config (user="admin",pass="1234",port="8080",BSSID="WIFI"):
    return "conectado a la red"
config(BSSID="A56",pass="12345678")
```

## CONOCIENDO *ARGS Y **KARGS (EMPAQUETADO Y DESEMPAQUETADO DE ARGUMENTOS POSICIONALES)

### DESEMPAQUETANDO ARGUMENTOS **POSICIONALES**

Esta tecnica nos permite empaquetar nuestros argumentos cuando no sabemos la cantidad de datos que vamos a pasar.Imaginemos que nos pide una funcion para sumar n cantidad de numeros la solucion seria empaquetar los argumentos y luego desempaquetarlos para ello en la definicion de la funcion detro de los parametros debemos usar el parametro `*` delante del nombre del parametro posicional esto hara que todos los argumentos se almacenan en una tupla (lista) esto nos permite recorer dentro de sus elementos para poder desempaquetarlo y realizar las operaciones necesarias.

```python
# Deseamos crear una funcion que nos permita sumar n cantidad de numeros
# n -> es un numero variable puede ser 3,7,8.....n

def suma (*args):
    # *args =(2,5,7,8,9)
    acumulado=0
    for i in args:
        acumulado += i
    return acumulado
print(suma(2,5,7,8,9))
```

## DESEMPAQUETANDO ARGUMENTOS **NOMINALES**

En este caso como en el anterior utilizaremos el operador `*` la casuistica es el mismo sin embargo para desempaquetar argumento nominales usaremos `**` delante del nombre del parametr nominal,diferrencia del anterior esto se empaquetara en un diccionario (`{clave:valor}`)

```python
# Debemos crear una funcion que me permita saber encontrar la persona con mayor calificacion.
def mejor_alumno(**kwargs):
    # **kwargs={'Noemmy'=20,'Eduardo'=18,'David'=1}
    for alumno,nota in kwargs.items():
        if nota > nota_maxima:
            nota_maxima = nota
            mejor_alumno = alumno
    return mejor_alumno
mejor_alumno(Noemmy=20,Eduardo=18,David=19)
```

## FUNCIONES ANONIMAS

Las funciones anonimas en python son llamadas `lambda` ,estas funciones tienen las siguientes propiedades:

1. Se escribe en una unica sentencia  `(linea)`.
2. No tiene nombre `(anonima)`.
3. Su cuerpo conlleva un `(return)` implicito.
4. Puede recibir cualquier numero de parametros.

La estructura para definir unaa funcion `lambda` es la siguiente:

1. Escribir la palabra reservada `lambda`.
2. Especificar la cantidad de parametros.
3. Indicar los datos de retorno.

```python
lambda a,b: a+b
```

> [!TIP] Puesto que esta funcion es anonima para ejecutarla debemos almacenar la funcion en una variable.

```python
suma=lambda a,b: a+b
suma(3,6)
```

## DOCUMENTACION

Python nos permite documentar una funcion con el objetivo de explicar mejor determinada zonas de nuestro codigo,para eso usamos una cadena de texto  despues de la definicion de una funcion ,a esta cadena de texto se le conoce como `docstring` y esta delimitado por triples `"""aqui el texto"""`.

```python
def suma (a,b):
    """
    Funcion para realizar la suma de dos numeros 
    """
# Los docstring tambien nos permite explicar los parametros que recibe y los datos de salida 
def resta (a,b):
    """ 
    a= a un numero entero.
    b= a un numero entero.
    En ambos casos a,b no deden recibir valores menores 0.
    Retornara un dato entero <int> positivo 
    """
    return a-b
```

> [!WARNING] En el proceso de documentacion tener encuenta de incluir a lo menos lo siguie:
> 1. Breve explicacion sobre que hace la funcion.
> 2. Especificaciones y caracteristicas de los parametros incluyendo sus tipos.
> 3. Restricciones de la funcion.  
> 4. El valor que retorna y sus caracteristicas.