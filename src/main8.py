
def rendimiento(puntuacion):
    if puntuacion == 0.0:
        nivel = "Inaceptable"
    elif puntuacion == 0.4:
        nivel = "Aceptable"
    else:
        nivel = "Meritorio"
    
    return nivel

def beneficios(puntuacion):
    if puntuacion == 0.0:
        beneficios = 0
    else:
        beneficios = 2400 * puntuacion

    return beneficios

if __name__ == "__main":
    try:
        puntuacion = float(input("Introduce tu puntuación: "))
        nivel = rendimiento(puntuacion)
        profit = beneficios(puntuacion)
        
        print(f"Tu nivel de rendimiento es: {nivel}")
        print(f"Recibiras {profit}€ en beneficios.")
    except ValueError:
        print("Error: Debes ingresar un valor valido para la puntuacion.")
