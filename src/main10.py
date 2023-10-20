def es_numero_primo(numero):
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

    try:
        numero = int(input("Ingrese un numero entero: "))
    except ValueError:
        print("Ingrese un numero entero valido.")

    if es_numero_primo(numero):
        print(f"{numero} es un numero primo.")
    else:
        print(f"{numero} no es un numero primo.")

