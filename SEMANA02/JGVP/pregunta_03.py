def cuadrados_pares(maximo):
    return [numero**2 for numero in range(1, maximo + 1) if numero % 2 == 0]


class GeneradorCuadrados:
    def __init__(self, maximo):
        self.maximo = maximo

    def obtener_cuadrados(self):
        return cuadrados_pares(self.maximo)


generador = GeneradorCuadrados(10)
resultado = generador.obtener_cuadrados()

print("Cuadrados de números pares:")
for valor in resultado:
    print(valor)
