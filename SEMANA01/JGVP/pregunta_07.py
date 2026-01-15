numeros_texto = input("Ingrese números separados por espacios: ")
numeros = [int(valor) for valor in numeros_texto.split()]


def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

primos = list(filter(es_primo, numeros))
cuadrados = list(map(lambda n: n * n, primos))

print("Primos:", primos)
print("Cuadrados de primos:", cuadrados)
