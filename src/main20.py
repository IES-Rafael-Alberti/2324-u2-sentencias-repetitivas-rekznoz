def buscar_letra_frase(frase, letra):
    for i, caracter in enumerate(frase):
        if caracter == letra:
            return i + 1
    return -1 

if __name__ == "__main__":
    frase = input("Ingresa una frase ")
    letra = input("Ingresa una letra a buscar ")

    posicion = buscar_letra_frase(frase, letra)

    if posicion > 0:
        print(f"La letra '{letra}' se encontro en la posicion {posicion} de la frase")
    else:
        print(f"No se encontro la letra '{letra}' en la frase")
