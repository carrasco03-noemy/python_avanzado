## 5. Empaquetado Nominal (**kwargs) Diseña una función llamada generar_perfil_usuario(**kwargs) que reciba datos arbitrarios en formato clave-valor
# (como nombre, edad, país, profesión) y devuelva una cadena de texto descriptiva que recorra el diccionario armado e imprima cada característica
# del usuario. 

def generar_perfil_usuario(**kwargs):
    for clave, valor in kwargs.items():
        print(clave, ":", valor)

generar_perfil_usuario(
    nombre="Ana",
    edad=20,
    pais="Peru",
    profesion="Estudiante")

