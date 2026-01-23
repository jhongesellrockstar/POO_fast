class ClasificadorProductos:
    def __init__(self, productos):
        self.productos = productos

    def clasificar(self):
        clasificacion = {"barato": [], "medio": [], "caro": []}
        for producto in self.productos:
            if producto["precio"] <= 10:
                clasificacion["barato"].append(producto["nombre"])
            elif producto["precio"] <= 50:
                clasificacion["medio"].append(producto["nombre"])
            else:
                clasificacion["caro"].append(producto["nombre"])
        return clasificacion


productos = [
    {"nombre": "Jugo", "precio": 4, "categoria": "bebida"},
    {"nombre": "Pizza", "precio": 18, "categoria": "comida"},
    {"nombre": "Laptop", "precio": 1200, "categoria": "tecnologia"},
    {"nombre": "Pan", "precio": 1, "categoria": "comida"},
    {"nombre": "Audifonos", "precio": 55, "categoria": "tecnologia"},
]

clasificador = ClasificadorProductos(productos)
clasificacion = clasificador.clasificar()

print("Clasificación por precio:")
for categoria, nombres in clasificacion.items():
    print(f"{categoria}:")
    for nombre in nombres:
        print(f"- {nombre}")
