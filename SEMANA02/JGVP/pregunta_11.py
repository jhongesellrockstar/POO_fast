ventas = [
    {"producto": "Cuaderno", "cantidad": 3, "precio": 5},
    {"producto": "Lapiz", "cantidad": 10, "precio": 1},
    {"producto": "Mochila", "cantidad": 2, "precio": 40},
    {"producto": "Agenda", "cantidad": 6, "precio": 8},
    {"producto": "Plumon", "cantidad": 7, "precio": 3},
]

ventas_mayores = list(filter(lambda venta: venta["cantidad"] > 5, ventas))

ingresos = list(
    map(
        lambda venta: {
            "producto": venta["producto"],
            "ingreso": venta["cantidad"] * venta["precio"],
        },
        ventas_mayores,
    )
)

print("Informe de ventas (cantidad > 5):")
for item in ingresos:
    print(f"{item['producto']}: {item['ingreso']}")
