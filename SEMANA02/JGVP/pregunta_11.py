class InformeVentas:
    def __init__(self, ventas):
        self.ventas = ventas

    def filtrar_ventas(self):
        return list(filter(lambda venta: venta["cantidad"] > 5, self.ventas))

    def calcular_ingresos(self, ventas_filtradas):
        return list(
            map(
                lambda venta: {
                    "producto": venta["producto"],
                    "ingreso": venta["cantidad"] * venta["precio"],
                },
                ventas_filtradas,
            )
        )

    def imprimir_informe(self, ingresos):
        print("Informe de ventas (cantidad > 5):")
        for item in ingresos:
            print(f"{item['producto']}: {item['ingreso']}")


ventas = [
    {"producto": "Cuaderno", "cantidad": 3, "precio": 5},
    {"producto": "Lapiz", "cantidad": 10, "precio": 1},
    {"producto": "Mochila", "cantidad": 2, "precio": 40},
    {"producto": "Agenda", "cantidad": 6, "precio": 8},
    {"producto": "Plumon", "cantidad": 7, "precio": 3},
]

informe = InformeVentas(ventas)
ventas_filtradas = informe.filtrar_ventas()
ingresos = informe.calcular_ingresos(ventas_filtradas)
informe.imprimir_informe(ingresos)
