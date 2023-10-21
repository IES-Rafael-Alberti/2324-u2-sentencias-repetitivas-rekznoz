def suma_digitos(numero):
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return suma


if __name__ == "__main__":

    numeros_pares = 0
    numero = 0
    while numero != -1 :
        try:
            numero = int(input("Ingresa un numero entero positivo (-1 para finalizar) "))
            if numero > 0:
                suma = suma_digitos(numero)
                print(f"La suma de los numeros {numero} es {suma}")
                if suma % 2 == 0:
                    numeros_pares += 1
            else:
                print("Ingresa un numero entero positivo valido")
        except ValueError:
            print("Ingresa un numero entero positivo valido")

    print(f"Hay {numeros_pares} numeros pares.")
