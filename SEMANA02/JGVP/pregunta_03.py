def cuadrados_pares(maximo):
    return [numero ** 2 for numero in range(1, maximo + 1) if numero % 2 == 0]


resultado = cuadrados_pares(10)
print("Cuadrados de números pares:")
for valor in resultado:
    print(valor)
