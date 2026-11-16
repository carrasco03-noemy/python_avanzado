## 8. Closure (Clausura) Escribe una función externa llamada crear_validador_limite(limite_maximo: int) que retorne una función interior.
# Esta función interior debe recibir un número y retornar True si es menor o igual al limite_maximo, o False si lo supera. Pon a prueba tu closure 
# creando un validador con límite 100.

def crear_validador_limite(limite_maximo: int):

    def validar(numero):
        if numero <= limite_maximo:
            return True
        else:
            return False

    return validar

validador = crear_validador_limite(100)

print(validador(80))
print(validador(120))