
def tipo_pizza(pizza):
    if pizza == "vegetariana":
        return True
    else:
        return False

def ingredientes_pizza(pizza,ingrediente):
    if pizza:
        if ingrediente == "pimiento" or ingrediente == "tofu":
            return True 
        else:
            return False
    elif not pizza:
        if ingrediente == "peperoni" or ingrediente == "jamon" or ingrediente == "salmon":
            return True 
        else:
            return False
    else:
        return False

if __name__ == "__main__":

    pizza = input("Que tipo de Pizza quieres (vegetariana/normal)\n").lower()
    tipo = tipo_pizza(pizza)

    if tipo:
        ingrediente = input("Selecciona uno de los Ingredientes (Pimiento/Tofu)\n").lower()
        if ingredientes_pizza(tipo,ingrediente):
            print("Seleccionaste pizza Vegetariana con Tomate, mozarella y " + ingrediente)
        else: 
            print("No tenemos pizza con esos ingredientes.")
    else:
        ingrediente = input("Selecciona uno de los Ingredientes (Peperoni/Jamon/Salmon)\n").lower()
        if ingredientes_pizza(tipo,ingrediente):
            print("Seleccionaste pizza con Tomate, mozarella y " + ingrediente)
        else: 
            print("No tenemos pizza con esos ingredientes.")