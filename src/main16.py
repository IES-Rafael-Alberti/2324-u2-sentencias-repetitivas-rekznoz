def numeros_enteros(entrada,numero):
    if entrada > 0:
        if entrada > numero:
            return entrada
    return numero


if __name__ == "__main__":
    numero = 0
    entrada = None
    while entrada != 0:
        try:
            entrada = int(input("Ingresa un numero entero (0 para finalizar):  "))
        except ValueError:
            print("Introduce un numero valido")
            
        if entrada != 0:
            numero = numeros_enteros(entrada,numero)
    
    print(numero)