## 9. Programación Funcional (map()) Dada una lista de precios en dólares: precios: list[float] = [10.5, 20.0, 50.0, 5.99], utiliza la función 
# integrada map() combinada con una función lambda para incrementar todos los precios en un 10% (multiplicarlos por 1.10). Recuerda envolver el
#  resultado en list() para visualizarlo.

precios: list[float] = [10.5, 20.0, 50.0, 5.99]

resultado = list(map(lambda precio: precio * 1.10, precios))

print("Precios aumentados:", resultado) 
