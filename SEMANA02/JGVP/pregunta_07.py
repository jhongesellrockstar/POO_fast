class CalculadoraPromedio:
    def __init__(self, listas):
        self.listas = listas

    def promedio(self, lista_numeros):
        return sum(lista_numeros) / len(lista_numeros)

    def mostrar_promedios(self):
        for lista in self.listas:
            resultado = self.promedio(lista)
            print(f"Promedio de {lista}: {resultado}")


listas = [
    [10, 12, 14],
    [5, 7, 9, 11],
    [20, 18],
]

calculadora = CalculadoraPromedio(listas)
calculadora.mostrar_promedios()
