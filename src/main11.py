def letras_invertidas(palabra):
    return palabra[::-1]

if __name__ == "__main__":
    palabra = input("Por favor, ingrese una palabra: ")
    letras = letras_invertidas(palabra)
    print("Letras de la palabra invertida:", letras)
