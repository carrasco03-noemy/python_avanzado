## 6. Funciones Anónimas (lambda) Crea una función anónima (lambda) asignada a una variable llamada es_par que reciba un número entero y devuelva
# True si es par y False en caso contrario. Pruébala pasando un número par y uno impar. 

es_par = lambda numero: numero % 2 == 0

print(es_par(8))
print(es_par(5))