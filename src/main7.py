def tipo_impositivo(renta_anual):
    if renta_anual < 10000:
        return 5
    elif 10000 <= renta_anual < 20000:
        return 15
    elif 20000 <= renta_anual < 35000:
        return 20
    elif 35000 <= renta_anual < 60000:
        return 30
    else:
        return 45

if __name__ == "__main__":
    try:
        renta_anual = float(input("Introduce tu renta anual "))
        tipo = tipo_impositivo(renta_anual)
        print(f"Tu tipo impositivo es {str(tipo)}%")
    except ValueError:
        print("Error: Debes ingresar un valor valido para la renta anual.")
