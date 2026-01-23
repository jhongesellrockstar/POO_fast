class TransformadorLista:
    def __init__(self, maximo):
        self.maximo = maximo

    def pares_al_cubo(self):
        numeros = list(range(1, self.maximo + 1))
        pares = [numero for numero in numeros if numero % 2 == 0]
        return list(map(lambda numero: numero**3, pares))


transformador = TransformadorLista(50)
resultado = transformador.pares_al_cubo()

print("Números pares al cubo:")
for valor in resultado:
    print(valor)
