def promedio(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)


listas = [
    [10, 12, 14],
    [5, 7, 9, 11],
    [20, 18],
]

for lista in listas:
    resultado = promedio(lista)
    print(f"Promedio de {lista}: {resultado}")
