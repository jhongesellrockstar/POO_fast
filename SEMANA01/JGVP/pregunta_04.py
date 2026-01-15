ventas = {
    "Producto A": [120, 150, 90],
    "Producto B": [80, 110, 70],
    "Producto C": [200, 180, 160],
}

totales = {}
for producto, lista_ventas in ventas.items():
    totales[producto] = sum(lista_ventas)

mayor_producto = max(totales, key=totales.get)

print("Total de ventas por producto:")
for producto, total in totales.items():
    print(f"- {producto}: {total}")

print(f"El producto con mayor ingreso es: {mayor_producto}")
