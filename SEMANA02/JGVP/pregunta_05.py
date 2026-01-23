class TransformadorNombres:
    def __init__(self, nombres):
        self.nombres = nombres

    def convertir_a_mayusculas(self):
        return list(map(lambda nombre: nombre.upper(), self.nombres))

    def crear_diccionario_longitudes(self, nombres_mayus):
        return {nombre: len(nombre) for nombre in nombres_mayus}


lista = TransformadorNombres(["ana", "luis", "marta", "jose"])

nombres_mayus = lista.convertir_a_mayusculas()
longitudes = lista.crear_diccionario_longitudes(nombres_mayus)

print("Nombres en mayúsculas:")
for nombre in nombres_mayus:
    print(nombre)

print("Diccionario de cantidades de letras:")
for nombre, cantidad in longitudes.items():
    print(f"{nombre}: {cantidad}")
