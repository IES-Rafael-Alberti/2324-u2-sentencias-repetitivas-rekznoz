from src.main25 import alabra_mas_larga

def test_encontrar_palabra_mas_larga_sin_palabras():
    palabra, cantidad = alabra_mas_larga("Hola")
    assert palabra == "Hola"
    assert cantidad == 1
    palabra, cantidad = alabra_mas_larga("La frase más larga")
    assert palabra == "frase"
    assert cantidad == 4
    palabra, cantidad = alabra_mas_larga("   Esto    es    un     ejemplo   ")
    assert palabra == "ejemplo"
    assert cantidad == 4