class ListaNombres:
    def __init__(self, nombres):
        self.nombres = nombres

    def a_mayusculas(self):
        return list(map(lambda nombre: nombre.upper(), self.nombres))

    def cantidades(self, nombres_mayus):
        return {nombre: len(nombre) for nombre in nombres_mayus}


lista = ListaNombres(["ana", "luis", "marta", "jose"])

nombres_mayus = lista.a_mayusculas()
cantidad_letras = lista.cantidades(nombres_mayus)

print("Nombres en mayúsculas:")
for nombre in nombres_mayus:
    print(nombre)

print("Diccionario de cantidades de letras:")
for nombre, cantidad in cantidad_letras.items():
    print(f"{nombre}: {cantidad}")
