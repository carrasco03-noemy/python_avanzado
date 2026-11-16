## 10. Programación Funcional (filter()) Dada una lista de palabras: palabras: list[str] = ["sol", "computadora", "luz", "programacion", "ia", 
# "python"], utiliza la función integrada filter() y una función lambda para filtrar y quedarte únicamente con aquellas palabras que tengan más
#  de caracteres. Muestra el resultado convertido en lista. 

palabras: list[str] = ["sol", "computadora", "luz", "programacion", "ia", "python"]

resultado = list(filter(lambda palabra: len(palabra) > 4, palabras))

print("Palabras con mas de 4 caracteres:", resultado)