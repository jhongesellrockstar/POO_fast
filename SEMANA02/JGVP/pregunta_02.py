class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota


estudiantes = [
    Estudiante("Ana", 15),
    Estudiante("Luis", 9),
    Estudiante("Marta", 18),
    Estudiante("Jose", 11),
]

for estudiante in estudiantes:
    if estudiante.nota >= 11:
        print(f"{estudiante.nombre} aprobó con {estudiante.nota}.")
    else:
        print(f"{estudiante.nombre} reprobó con {estudiante.nota}.")
