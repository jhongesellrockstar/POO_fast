CLAVE_CORRECTA = "python123"
intentos = 0

while intentos < 3:
    clave = input("Ingrese la contraseña: ")
    if clave == CLAVE_CORRECTA:
        print("Acceso permitido.")
        break
    intentos += 1
    print("Contraseña incorrecta.")

if intentos == 3:
    print("Acceso bloqueado. Se agotaron los intentos.")
