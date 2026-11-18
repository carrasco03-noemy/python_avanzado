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

## TYPE_HINTS (ANOTACIONES DE TIPO)

Nos permite indicar que tipo de dato que tendra una variable,parametro y el valor de retorno de una funcion.
Para utilizarlos debemos de indicar el tipo de dato despues del separador `:`, en el caso de valor retorno usaremos `->` luego el tipo de dato y finalmente el separador `:` que indica el inicio del bloque de codigo de la funcion.
Las `anotaciones de tipo` son una herramienta que nos permite complementar la documentacion de nuestro codigo.
**TENEMOS LOS SIGUIENTES**

- **SIMPLES**
   -int -> numero enteros
   -float -> numeros decimales
   -bool -> datos boleanos (verdad o falso)
   -str -> datos de tipo texto o cadena
   -list -> listas `[]`
   -tuple -> tuplas `()`
   -dict -> diccionarios `{}`

- **COMPUESTOS**
   Existen casos en los que necesitamos mas expresividad en la *anotacion de tipos* ¿que ocurre si queremos indicar una *lista de cadenas* o un *conjunto de enteros*.?
   -list[str] -> lista de cadenas de texto.
   -list[int] -> lista de numeros enteros.
   -dict[str,float] -> diccionario donde las claves son cadenas de texto y los valores son flotantes/decimales.

- **MULTIPLES**
  En el caso que queramos indicar de un determinado parametro puede ser de un `tipo o de otro` tenemos que especificarlo usando el operador `|`
  - tuple|dict -> puede ser dato de tipo tupla o diccionario
  - list[str|int] -> lista cuyos elementos pueden ser cadenas de texto o enteros.
  - dicts[str|int,float|int]-> diccionario cuya clave puede ser cadena o entero cuyo valor puede ser flotante o entero.

## CLOSURE

Una `closure` o `clausura` sus funciones que establecen una funcion interior ,o retornan un funcion estas funciones se caracterisan por recordar el valor de los argumentos que se le pasa .

```python
def producto(n):
    def multiplicador 
    return n*m
    return multiplicador
```

## PROGRAMACION FUNCIONAL

python es un ineguaje de programacion multiparadigma que mejor funcion tienen es la funcional.
python usa tres `map()`,`filter()`,`reduce()`, pero nosotros solo usarmos `map()`,`filter()`.
estas funciones integradas de python siirven para procesar y transformar colecciones de datos (listas,diccionarios) de manera muy eficiente:
>[!TIP] Importante:
> las funciones map()`y`filter() resiven dos parametros primero la funcion a ejecutar y segundo el iterable en que va actuar. la funcion que recive como parametro puede ser normal (`def`) o puede ser anonima (`lambda`).

### 1. MAP ()

map aplica una funcion especifica a cada uno de los elementos de una coleccion (iterable) y devuelve un nuevo iterable con los resultados.

```python
# de una lista de numeros deseamos calcular la potencia de cada numero
numero:list[int]=[2,4,6,8,7]
## cuando deceamos trabajar con funciones anoonima tenemos que declarar primero la funcion antes de pararla por parametro
def f(X):
    return x**2
## una ves creada pasamos la funcion como parametro
map(f,numeros)
## cuando deseamos trabajar con funciones anonimas usamos lambda dentro del parametro
map(lambda x:x**2,numeros)

### 2. filter()
filter pasa cada elemento de una coleccion por una funcion y solo se queda con aquellos elementos dende la funcion devuelva true (es decir, filtra los datos segun una condicion).
```

```python
# imagina que tienes una lista de numeros y solo quieres quedarte con los numeros pares.
numeros:list[int]=[2,7,8,20,4,3,9,12,11,16,17]
filter(lambda n:n % 2== 0,numeros)
```

>[!WARNING]nota importante
> tanto map()`como`filter() no devuelven listas directamente, si no iteradores. esto es para ahorrar memoria (evaluacion perezosa o lazy evaluacion). si quieres ver el resultado como una lista tradicional, siempre debes envolver en list.

## COMPRENSION DE LISTA


List Comprehension es una forma sencilla y rápida de crear nuevas listas utilizando una sola línea de código, en lugar de escribir muchas líneas con el ciclo FOR.

1. List Comprehension básico

Permite crear una nueva lista realizando operaciones con los elementos de otra lista.

Ejemplo: elevar los números al cuadrado.

numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]
print(cuadrados)

Resultado: "[1, 4, 9, 16, 25]"

2. List Comprehension con IF

Permite seleccionar elementos que cumplen una condición.

Ejemplo: obtener solamente los números pares.

numeros = [1, 2, 3, 4, 5]
pares = [x for x in numeros if x % 2 == 0]
print(pares)

Resultado: "[2, 4]"

3. List Comprehension anidado

Permite crear listas dentro de otras listas, como una matriz, utilizando dos ciclos FOR.

Ejemplo:

matriz = [[j for j in range(1, 4)] for i in range(3)]
print(matriz)

Resultado:

[[1, 2, 3],
 [1, 2, 3],
 [1, 2, 3]]

Conclusión:

List Comprehension es una herramienta de Python que permite crear listas, realizar operaciones y aplicar condiciones de manera más fácil, rápida y con menos líneas de código.

## DICCIONARIOS POR COMPRENSION

Los diccionarios por comprensión permiten crear nuevos diccionarios de manera sencilla y rápida utilizando una sola línea de código. Se pueden crear elementos con una clave y un valor a partir de otros datos.

1. Diccionario básico por comprensión

Permite crear un diccionario a partir de una lista.

Ejemplo:

numeros = [1, 2, 3, 4, 5]
cuadrados = {x: x**2 for x in numeros}
print(cuadrados)

Resultado:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

2. Diccionario con IF

Permite agregar solamente los elementos que cumplen una condición.

Ejemplo: guardar solo los números pares.

numeros = [1, 2, 3, 4, 5]
pares = {x: x for x in numeros if x % 2 == 0}
print(pares)

Resultado:

{2: 2, 4: 4}

3. Diccionario con operaciones

Permite realizar operaciones con los valores al crear el diccionario.

Ejemplo: multiplicar cada número por dos.

numeros = [1, 2, 3]
dobles = {x: x*2 for x in numeros}
print(dobles)

Resultado:

{1: 2, 2: 4, 3: 6}

Conclusión:

Los diccionarios por comprensión permiten crear diccionarios en una sola línea de código, utilizando condiciones y operaciones. Su estructura utiliza llaves "{}" y permite guardar datos mediante claves y valores.