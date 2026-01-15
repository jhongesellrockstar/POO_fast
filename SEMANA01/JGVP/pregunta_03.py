numeros_texto = input("Ingrese números separados por espacios: ")
numeros = [int(valor) for valor in numeros_texto.split()]

sin_duplicados = []
for numero in numeros:
    if numero not in sin_duplicados:
        sin_duplicados.append(numero)

print("Lista sin duplicados:", sin_duplicados)
