class Aula:
    def __init__(self, alumnos):
        self.alumnos = alumnos

    def promedios(self):
        return list(
            map(
                lambda alumno: sum(alumno["notas"]) / len(alumno["notas"]),
                self.alumnos,
            )
        )

    def aprobados(self, promedios):
        return list(filter(lambda datos: datos[1] >= 6, zip(self.alumnos, promedios)))

    def diccionario_promedios(self, aprobados):
        return {alumno["nombre"]: promedio for alumno, promedio in aprobados}

    def imprimir_estado(self, promedios):
        print("Estado de cada alumno:")
        for alumno, promedio in zip(self.alumnos, promedios):
            if promedio >= 6:
                print(f"{alumno['nombre']} aprobado")
            else:
                print(f"{alumno['nombre']} reprobado")


alumnos = [
    {"nombre": "Ana", "notas": [8, 7, 9]},
    {"nombre": "Luis", "notas": [4, 5, 6]},
    {"nombre": "Marta", "notas": [10, 9, 8]},
    {"nombre": "Jose", "notas": [6, 6, 6]},
]

curso = Aula(alumnos)
promedios = curso.promedios()
alumnos_aprobados = curso.aprobados(promedios)
promedios_dict = curso.diccionario_promedios(alumnos_aprobados)

print("Promedios de alumnos aprobados:")
for nombre, promedio in promedios_dict.items():
    print(f"{nombre}: {promedio}")

curso.imprimir_estado(promedios)
