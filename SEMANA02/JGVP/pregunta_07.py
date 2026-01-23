def promedio(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)


class CalculadoraPromedios:
    def __init__(self, listas):
        self.listas = listas

    def mostrar_promedios(self):
        for lista in self.listas:
            resultado = promedio(lista)
            print(f"Promedio de {lista}: {resultado}")


listas = [
    [10, 12, 14],
    [5, 7, 9, 11],
    [20, 18],
]

calculadora = CalculadoraPromedios(listas)
calculadora.mostrar_promedios()
