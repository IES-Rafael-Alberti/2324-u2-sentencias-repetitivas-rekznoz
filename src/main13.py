def concatenar_frase(palabra,frase):
    frase += palabra + " "
    return frase

if __name__ == "__main__":

    frase = ""
    entrada = ""
    while entrada != "salir":
        entrada = input("Escribe algo (o 'salir' para finalizar): ")
        if entrada != "salir":
            frase = concatenar_frase(entrada,frase)
    
    print(frase)