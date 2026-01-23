nombres = ["ana", "luis", "marta", "jose"]

nombres_mayus = list(map(lambda nombre: nombre.upper(), nombres))

cantidad_letras = {nombre: len(nombre) for nombre in nombres_mayus}

print("Nombres en mayúsculas:")
for nombre in nombres_mayus:
    print(nombre)

print("Diccionario de cantidades de letras:")
for nombre, cantidad in cantidad_letras.items():
    print(f"{nombre}: {cantidad}")
