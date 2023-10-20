def crear_triangulo(numero_filas):
    if numero_filas < 1:
        return ""

    triangulo = ""
    for i in range(1, numero_filas + 1):
        triangulo += "*" * i
        triangulo += "\n"
    
    return triangulo
    
if __name__ == "__main__":
    numero_filas = int(input("Introduce el numero de filas del triangulo "))
    triangulo = crear_triangulo(numero_filas)
    
    print(triangulo)
