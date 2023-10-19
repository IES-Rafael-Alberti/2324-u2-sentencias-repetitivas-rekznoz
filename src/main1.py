
def repetir_palabra(palabra, repeticiones):
    return palabra * repeticiones

if __name__ == "__main__":
    palabra = input("Introduce una palabra ")
    resultado = repetir_palabra(palabra, 10)
    print(resultado)
