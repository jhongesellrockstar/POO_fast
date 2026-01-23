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
        estado = "aprobó"
    else:
        estado = "reprobó"
    print(f"{estudiante.nombre} {estado} con {estudiante.nota}.")
