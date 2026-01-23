class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria


productos = [
    Producto("Jugo", 4, "bebida"),
    Producto("Pizza", 18, "comida"),
    Producto("Laptop", 1200, "tecnologia"),
    Producto("Pan", 1, "comida"),
    Producto("Audifonos", 55, "tecnologia"),
]

clasificacion = {"barato": [], "medio": [], "caro": []}

for producto in productos:
    if producto.precio <= 10:
        clasificacion["barato"].append(producto.nombre)
    elif producto.precio <= 50:
        clasificacion["medio"].append(producto.nombre)
    else:
        clasificacion["caro"].append(producto.nombre)

print("Clasificación por precio:")
for categoria, nombres in clasificacion.items():
    print(f"{categoria}:")
    for nombre in nombres:
        print(f"- {nombre}")
