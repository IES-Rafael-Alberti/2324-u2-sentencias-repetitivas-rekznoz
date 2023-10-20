def tabla_de_multiplicar(numero):
    tabla = ""
    for i in range(1, 11):
        resultado = numero * i
        tabla += f"{numero} x {i} = {resultado}\n"
    return tabla

if __name__ == "__main__":

    tabla_completa = ""
    
    for i in range(1, 11):
        tabla_completa += f"Tabla del {i}:\n"
        tabla_completa += tabla_de_multiplicar(i)

    print(tabla_completa)
