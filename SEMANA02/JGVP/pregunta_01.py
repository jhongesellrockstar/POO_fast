class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria


productos = [
    Producto("Cuaderno", 8, "utiles"),
    Producto("Lapiz", 3, "utiles"),
    Producto("Mochila", 45, "accesorios"),
    Producto("Borrador", 2, "utiles"),
    Producto("Agenda", 12, "utiles"),
]

productos_caros = {
    producto.nombre: producto.precio
    for producto in productos
    if producto.precio > 10
}

print("Productos con precio mayor a 10:")
for nombre, precio in productos_caros.items():
    print(f"- {nombre}: {precio}")
