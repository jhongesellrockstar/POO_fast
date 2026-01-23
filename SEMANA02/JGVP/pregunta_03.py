class GeneradorCuadrados:
    def __init__(self, maximo):
        self.maximo = maximo

    def cuadrados_pares(self):
        return [
            numero ** 2
            for numero in range(1, self.maximo + 1)
            if numero % 2 == 0
        ]


generador = GeneradorCuadrados(10)
resultado = generador.cuadrados_pares()

print("Cuadrados de números pares:")
for valor in resultado:
    print(valor)
