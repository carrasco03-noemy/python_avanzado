## 2. Parámetros Nominales y por Defecto Crea una función llamada calcular_precio_final que calcule el precio de un producto aplicando un impuesto
# y un descuento opcional.● Parámetros por defecto: impuesto = 0.18 (18%) y descuento = 0.0. ● Utiliza argumentos nominales en su llamada para
# aplicar solo un descuento del 0.05 (5%) manteniendo el impuesto por defecto.

def calcular_precio_final(precio, impuesto=0.10, descuento=0.0):
    total = precio + (precio * impuesto)
    total = total - (total * descuento)
    return total

resultado = calcular_precio_final(50, descuento=0.05)

print("El precio final es:", resultado)