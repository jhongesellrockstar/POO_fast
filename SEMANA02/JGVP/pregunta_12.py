class Alumno:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas


def calcular_promedio(alumno):
    return sum(alumno.notas) / len(alumno.notas)


alumnos = [
    Alumno("Ana", [8, 7, 9]),
    Alumno("Luis", [4, 5, 6]),
    Alumno("Marta", [10, 9, 8]),
    Alumno("Jose", [6, 6, 6]),
]

promedios = list(map(calcular_promedio, alumnos))

aprobados = list(filter(lambda datos: datos[1] >= 6, zip(alumnos, promedios)))

promedios_dict = {alumno.nombre: promedio for alumno, promedio in aprobados}

print("Promedios de alumnos aprobados:")
for nombre, promedio in promedios_dict.items():
    print(f"{nombre}: {promedio}")

print("Estado de cada alumno:")
for alumno, promedio in zip(alumnos, promedios):
    if promedio >= 6:
        print(f"{alumno.nombre} aprobado")
    else:
        print(f"{alumno.nombre} reprobado")
