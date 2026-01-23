personas = [
    ("Ana", 17),
    ("Luis", 20),
    ("Marta", 15),
    ("Jose", 30),
]

clasificacion = {
    nombre: "menor de edad" if edad < 18 else "mayor de edad"
    for nombre, edad in personas
}

print("Clasificación por edad:")
for nombre, estado in clasificacion.items():
    print(f"{nombre}: {estado}")
