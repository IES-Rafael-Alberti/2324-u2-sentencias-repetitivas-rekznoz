def suma_digitos(numero):
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return suma

if __name__ == "__main__":

    try:
        numero = int(input("Ingresa un numero entero positivo "))
        if numero < 0:
            raise ValueError
        resultado = suma_digitos(numero)
        print(f"La suma de los numeros {numero} es {resultado}")
    except ValueError:
        print("Introduce un numero valido")

