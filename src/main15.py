def sumas_enteros(numero,suma):
    if numero > 0:
        suma += numero
    return suma

if __name__ == "__main__":

    suma = 0
    entrada = None
    while entrada != 0:
        try:
            entrada = int(input("Ingresa un numero entero (0 para finalizar):  "))
        except ValueError:
            print("Introduce un numero valido")
            
        if entrada != 0:
            suma = sumas_enteros(entrada,suma)
    
    print(suma)