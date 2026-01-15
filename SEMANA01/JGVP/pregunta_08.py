empleados = [
    {"nombre": "Ana", "edad": 28, "salario": 1200},
    {"nombre": "Luis", "edad": 35, "salario": 1500},
    {"nombre": "Carla", "edad": 42, "salario": 1800},
]

actualizados = []
for empleado in empleados:
    if empleado["edad"] > 30:
        salario_nuevo = empleado["salario"] * 1.10
        actualizados.append({"nombre": empleado["nombre"], "salario": salario_nuevo})

print("Empleados mayores de 30 con salario actualizado:")
for empleado in actualizados:
    print(f"- {empleado['nombre']}: {empleado['salario']:.2f}")
