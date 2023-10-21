def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False

    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6

    return True

if __name__ == "__main__":
    numeros_primos = 0
    numero = None
    while numero != 0:
        try:
            numero = int(input("Ingresa un numero mayor que 1 (0 para finalizar) "))
            if numero > 1:
                if es_primo(numero):
                    numeros_primos += 1
            else:
                print("ingresa un numero mayor que 1.")

        except ValueError:
            print("ingresa un numero valido.")

    print(f"Se ingresaron {numeros_primos} numero primos.")