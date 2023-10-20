def validar_contrasena(entrada,contrasena):
    if entrada == contrasena:
        return True
    return False

if __name__ == "__main__":
    
    entrada = input("Ingrese la contraseña: ")
    contrasena = "pass1234"
    resultado = validar_contrasena(entrada,contrasena)
    if resultado:
        print("Contraseña correcta.")
    else:
        print("Acceso denegado.")

