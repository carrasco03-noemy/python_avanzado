## CREAR UNA FUNCION TIPO CLOSURE QUE ME PERMITA INNGRESAR NOMBRE ,APELLIDO Y ME RETORNE UN MENSAJE CON AMBOS DATOS .
 
def creador (nombre:str):
    def apellido(ap:str):
        return f"tu nombre es: {nombre} y tu apellido es {ap}"
    return apellido

alumno1=creador("David") # def apellido(ap): return
alumno2=creador("Noemy")
print(alumno1("Goliat"))
print(alumno2("Maikel"))

## USANDO CLOSURE CREAR UN FUNCION MULTIPLICADOR QUE RESIVA POR PARAMETRO EL FACTOR QUE DEVUELVA UNA FUNCION QUE PERMITA MULTIPLICAR CUALQUIER
#  NUMERO POR EL FACTOTR
def multiplicador (factor):
    def multiplicar(numero):
        return numero*factor
    return multiplicar

doble=multiplicador(4)
triple=multiplicador(6)
print(doble(5))
print(triple(5))

