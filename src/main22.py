def contar_pares_impares(numero):
    pares = 0
    impares = 0
    while numero > 0:
        digito = numero % 10
        if digito % 2 == 0:
            pares += 1
        else:
            impares += 1
        numero //= 10
    return pares, impares

if __name__ == "__main__":

    pares_totales = 0
    impares_totales = 0
    numero = None

    while numero != 0:
        try:
            numero = int(input("Ingresa un numero positivo (0 para finalizar): "))
            if numero < 0:
                print("Ingrese un numero positivo valido.")

            pares, impares = contar_pares_impares(numero)
            pares_totales += pares
            impares_totales += impares

            print(f"Digitos pares {pares} | Digitos impares {impares}")

        except ValueError:
            print("Ingrese un numero valido.")

    print(f"Total de digitos pares leidos {pares_totales}")
    print(f"Total de digitos impares leidos {impares_totales}")
