matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

diagonal = [matriz[i][i] for i in range(len(matriz))]

print("Diagonal principal:", diagonal)
