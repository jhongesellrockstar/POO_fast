class Empresa:
    def __init__(self, empleados):
        self.empleados = empleados

    def empleados_con_sueldo_mayor(self, sueldo_minimo):
        return {
            empleado["nombre"]: empleado["sueldo"]
            for empleado in self.empleados
            if empleado["sueldo"] > sueldo_minimo
        }


empleados = [
    {"nombre": "Ana", "sueldo": 1200},
    {"nombre": "Luis", "sueldo": 900},
    {"nombre": "Marta", "sueldo": 1500},
    {"nombre": "Jose", "sueldo": 800},
]

empresa = Empresa(empleados)
resultado = empresa.empleados_con_sueldo_mayor(1000)

print("Empleados con sueldo mayor a 1000:")
for nombre, sueldo in resultado.items():
    print(f"{nombre}: {sueldo}")
