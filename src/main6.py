def obtener_grupo(nombre, sexo):
    if (sexo == "mujer" and nombre.lower() < 'm') or (sexo == "hombre" and nombre.lower() > 'n'):
        return "A"
    else:
        return "B"

if __name__ == "__main__":
    nombre = input("Introduce tu nombre ").lower()
    sexo = input("Introduce tu sexo (mujer/hombre) ").lower()
    
    if sexo not in ["mujer", "hombre"]:
        print("Error: Debes ingresar 'mujer' o 'hombre' como sexo.")
    else:
        grupo = obtener_grupo(nombre, sexo)
        print(f"Tu grupo es: {grupo}")
