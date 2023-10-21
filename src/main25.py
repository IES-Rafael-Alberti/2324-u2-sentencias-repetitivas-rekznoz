def alabra_mas_larga(frase):
    palabras = frase.split()
    if not palabras:
        return None,
    palabra_mas_larga = max(palabras, key=len)
    return palabra_mas_larga, len(palabras)

if __name__ == "__main__":
    frase = input("Ingresa una frase ")
    palabra_mas_larga, cantidad_de_palabras = alabra_mas_larga(frase)

    if palabra_mas_larga is not None:
        print(f"Palabra larga es '{palabra_mas_larga}'")
        print(f"Total de palabras  {cantidad_de_palabras}")
    else:
        print("No se ingresaron palabras en la frase.")