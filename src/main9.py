def calcular_precio_entrada(edad):
    if edad < 4:
        precio = 0
    elif 4 <= edad <= 18:
        precio = 5
    else:
        precio = 10
    return precio

if __name__ == "__main__":
    try:
        edad = int(input("Introduce la edad del cliente: "))
        precio_entrada = calcular_precio_entrada(edad)
        print(f"El precio de la entrada es {precio_entrada}€")
    except ValueError:
        print("Error: Debes ingresar una edad valida.")
