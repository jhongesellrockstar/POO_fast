numeros = list(range(1, 51))

pares = [numero for numero in numeros if numero % 2 == 0]

pares_al_cubo = list(map(lambda numero: numero ** 3, pares))

print("Números pares al cubo:")
for valor in pares_al_cubo:
    print(valor)
