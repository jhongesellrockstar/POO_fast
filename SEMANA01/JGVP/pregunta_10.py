categorias = {
    "A": [60, 55, 70],
    "B": [40, 45, 35],
    "C": [90, 85, 95],
}

promedios = {clave: sum(valores) / len(valores) for clave, valores in categorias.items()}

categorias_mayores = dict(
    filter(lambda item: item[1] > 50, map(lambda item: (item[0], item[1]), promedios.items()))
)

print("Promedios por categoría:")
for categoria, promedio in promedios.items():
    print(f"- {categoria}: {promedio:.2f}")

print("Categorías con promedio mayor a 50:")
print(list(categorias_mayores.keys()))
