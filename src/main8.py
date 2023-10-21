def generar_triangulo(numero):
    triangulo = ""
    for i in range(1, numero + 1):
        linea = " ".join(str(j) for j in range(i, 0, -2) if j % 2 != 0)
        triangulo += linea + "\n"
    return triangulo

if __name__ == "__main__":
    
    try:
        numero = int(input("Un numero entero "))
        if numero < 1:
            raise ValueError
    except ValueError:
        print("Pon un numero entero valido.")

    triangulo = generar_triangulo(numero)
    print(triangulo)
