# Crear un programa que asigne un puntaje a cada letra del abesedarios
#  y que un funcion me permita saber la letra que tenga mejor puntaje ,mayor puntaje y la media 

def puntajes(**letras):
    mayor = 0
    letra_mayor = ""
    suma = 0
    for letra, puntaje in letras.items():
        suma = suma + puntaje
        if puntaje > mayor:
            mayor = puntaje
            letra_mayor = letra
    promedio = suma / len(letras)
    print("Letra con mayor puntaje:", letra_mayor)
    print("Mayor puntaje:", mayor)
    print("Promedio:", promedio)

puntajes(a=2, b=5, c=8, d=4, e=6)