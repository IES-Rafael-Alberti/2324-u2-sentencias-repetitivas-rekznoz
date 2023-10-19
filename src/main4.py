def cuenta_atras_desde(n):
    if n < 0:
        return []
    return [str(numero) for numero in range(n, -1, -1)]

if __name__ == "__main__":
    numero = int(input("Ingresa un número entero positivo: "))
    cuenta_atras = cuenta_atras_desde(numero)
    if cuenta_atras:
        print("Cuenta atras")
        print(", ".join(cuenta_atras))
    else:
        print("No hay cuenta para mostrar.")
