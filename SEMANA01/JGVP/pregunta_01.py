numeros_texto = input("Ingrese números enteros separados por espacios: ")
numeros = [int(valor) for valor in numeros_texto.split()]

if numeros == sorted(numeros):
    print("La lista está ordenada de forma ascendente.")
elif numeros == sorted(numeros, reverse=True):
    print("La lista está ordenada de forma descendente.")
else:
    print("La lista no está ordenada.")
