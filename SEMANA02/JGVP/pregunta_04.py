numeros = [1, 3, 4, 6, 7, 9, 10, 12, 15]

multiplos_de_tres = list(filter(lambda numero: numero % 3 == 0, numeros))

print("Múltiplos de 3:")
indice = 0
while indice < len(multiplos_de_tres):
    print(multiplos_de_tres[indice])
    indice += 1
