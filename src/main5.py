
def calcular_capital_inversion(inversion, tasa_interes, anos):
    capital_por_ano = []
    for _ in range(anos):
        inversion *= (1 + tasa_interes)
        capital_por_ano.append(round(inversion, 2))
    return capital_por_ano

if __name__ == "__main__":
    inversion = float(input("Ingresa una cantidad a invertir "))
    tasa_interes = float(input("Ingresa el porcentaje de interes anual ")) / 100
    anos = int(input("Ingresa un numero de años de la inversión: "))

    capital_por_ano = calcular_capital_inversion(inversion, tasa_interes, anos)

    print("Capital obtenido por año")
    for ano, capital in enumerate(capital_por_ano, start=1):
        print(f"Año {ano}: ${capital:.2f}")
