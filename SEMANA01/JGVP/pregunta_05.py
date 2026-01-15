numeros_texto = input("Ingrese números separados por espacios: ")
numeros = [int(valor) for valor in numeros_texto.split()]

combinaciones = []
for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        combinaciones.append((numeros[i], numeros[j]))

print("Combinaciones posibles:")
for par in combinaciones:
    print(par)
