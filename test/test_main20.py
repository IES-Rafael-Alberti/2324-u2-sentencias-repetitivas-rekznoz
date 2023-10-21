from src.main20 import buscar_letra_frase

def test_buscar_letra_frase():
    assert buscar_letra_frase("Hola", "o") == 2
    assert buscar_letra_frase("Rafael", "l") == 6