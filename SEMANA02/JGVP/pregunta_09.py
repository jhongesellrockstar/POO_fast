class RegistroPersonas:
    def __init__(self, personas):
        self.personas = personas

    def clasificar(self):
        return {
            nombre: "menor de edad" if edad < 18 else "mayor de edad"
            for nombre, edad in self.personas
        }


personas = [
    ("Ana", 17),
    ("Luis", 20),
    ("Marta", 15),
    ("Jose", 30),
]

registro = RegistroPersonas(personas)
clasificacion = registro.clasificar()

print("Clasificación por edad:")
for nombre, estado in clasificacion.items():
    print(f"{nombre}: {estado}")
