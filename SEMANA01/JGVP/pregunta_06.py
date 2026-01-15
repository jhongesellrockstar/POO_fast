palabras_texto = input("Ingrese palabras separadas por comas: ")
palabras = [palabra.strip() for palabra in palabras_texto.split(",")]

vocales = ("a", "e", "i", "o", "u")
resultado = []
for palabra in palabras:
    if (
        palabra
        and palabra[0].lower() in vocales
        and len(palabra) > 4
        and palabra not in resultado
    ):
        resultado.append(palabra)

print("Palabras filtradas:", resultado)
