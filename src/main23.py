def contar_digitos_en_linea(linea):
    digitos = 0
    for caracter in linea:
        if caracter.isdigit():
            digitos += 1
    return digitos

if __name__ == "__main__":

    lineas_completas = 0
    linea = None 

    while linea != "*":
        if linea == "/":
            if lineas_completas > 0:
                print(f"Linea completa {contar_digitos_en_linea(linea)} numeros.")
            else:
                print("No se introducio ninguna linea completa.")
            lineas_completas += 1
        else:
            if lineas_completas == 0:
                print("No se puede ingresar un título antes de una linea completa.")
            else:
                print("Título ingresado: ", linea)

        linea = input("Libro: ")

    print(f"Fin Se leyeron {lineas_completas} lineas completas.")