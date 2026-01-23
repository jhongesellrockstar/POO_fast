class FiltradorNumeros:
    def __init__(self, numeros):
        self.numeros = numeros

    def obtener_multiplos_de_tres(self):
        return list(filter(lambda numero: numero % 3 == 0, self.numeros))


lista = FiltradorNumeros([1, 3, 4, 6, 7, 9, 10, 12, 15])
multiplos_de_tres = lista.obtener_multiplos_de_tres()

print("Múltiplos de 3:")
indice = 0
while indice < len(multiplos_de_tres):
    print(multiplos_de_tres[indice])
    indice += 1
