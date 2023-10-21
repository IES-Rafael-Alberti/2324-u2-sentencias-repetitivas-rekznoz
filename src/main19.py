
def load_menu(opcion):
    if opcion == '1':
        return 1
    elif opcion == '2':
        return 2
    elif opcion == '3':
        return 3
    else:
        return 0

if __name__ == "__main__":

    opcion = 0

    while opcion != 3:

        print("Menu")
        print("1 - Comenzar programa")
        print("2 - Imprimir listado")
        print("3 - Finalizar programa")

        opcion = input("Elige una opcion (1, 2 o 3): ")
        opcion = load_menu(opcion)

        if opcion == 1:
            print("Comenzar programa")
        elif opcion == 2:
            print("Imprimir listado")
        elif opcion == 3:
            print("Finalizar programa")
        else:
            print("Opción incorrecta ! selecciona una opcion valida (1 2 o 3)")

