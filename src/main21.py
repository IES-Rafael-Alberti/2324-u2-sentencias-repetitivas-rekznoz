def calcular_total_compras(compras):
    total = sum(compras)
    if total > 1000:
        total *= 0.9
    return total

if __name__ == "__main__":
    entrada = None
    compras = []
    while entrada != 0:
        try:
            entrada = float(input("Ingrese un numero de la compra (0 para finalizar): "))
            if entrada < 0:
                print("No se pueden ingresar numeros negativos.")
            else:
                compras.append(entrada)
        except ValueError:
            print("Ingresa un monto valido (número).")
    
    total = calcular_total_compras(compras)
    print(f"Total a pagar {total}")