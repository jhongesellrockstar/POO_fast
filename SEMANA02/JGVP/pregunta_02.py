class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def estado(self):
        if self.nota >= 11:
            return "aprobó"
        return "reprobó"


estudiantes = [
    Estudiante("Ana", 15),
    Estudiante("Luis", 9),
    Estudiante("Marta", 18),
    Estudiante("Jose", 11),
]

for estudiante in estudiantes:
    print(f"{estudiante.nombre} {estudiante.estado()} con {estudiante.nota}.")
