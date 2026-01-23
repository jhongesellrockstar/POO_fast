class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo


def empleados_con_sueldo_mayor(empleados, sueldo_minimo):
    return {
        empleado.nombre: empleado.sueldo
        for empleado in empleados
        if empleado.sueldo > sueldo_minimo
    }


empleados = [
    Empleado("Ana", 1200),
    Empleado("Luis", 900),
    Empleado("Marta", 1500),
    Empleado("Jose", 800),
]

resultado = empleados_con_sueldo_mayor(empleados, 1000)

print("Empleados con sueldo mayor a 1000:")
for nombre, sueldo in resultado.items():
    print(f"{nombre}: {sueldo}")
