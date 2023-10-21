def numeros_impares_hasta(n):
    if n < 1:
        return []
    return [str(numero) for numero in range(1, n + 1, 2)]

if __name__ == "__main__":
    numero = int(input("Ingresa un número entero positivo "))
    impares = numeros_impares_hasta(numero)
    if impares:
        print("Numeros impares")
        print(", ".join(impares))
    else:
        print("No hay numeros para mostrar.")
