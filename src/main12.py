def contar_letra_en_frase(frase, letra):
    contador = 0
    for caracter in frase:
        if caracter == letra:
            contador += 1
    return contador

if __name__ == "__main__":
    frase = input("Por favor, ingrese una frase: ")
    letra = input("Por favor, ingrese una letra: ")
    cantidad = contar_letra_en_frase(frase, letra)
    print(f'La letra "{letra}" aparece {cantidad} veces en la frase.')
