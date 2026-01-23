class Inventario:
    def __init__(self, productos):
        self.productos = productos

    def productos_caros(self, minimo):
        return {
            producto["nombre"]: producto["precio"]
            for producto in self.productos
            if producto["precio"] > minimo
        }


productos = [
    {"nombre": "Cuaderno", "precio": 8, "categoria": "utiles"},
    {"nombre": "Lapiz", "precio": 3, "categoria": "utiles"},
    {"nombre": "Mochila", "precio": 45, "categoria": "accesorios"},
    {"nombre": "Borrador", "precio": 2, "categoria": "utiles"},
    {"nombre": "Agenda", "precio": 12, "categoria": "utiles"},
]

inventario = Inventario(productos)
productos_caros = inventario.productos_caros(10)

print("Productos con precio mayor a 10:")
for nombre, precio in productos_caros.items():
    print(f"- {nombre}: {precio}")
