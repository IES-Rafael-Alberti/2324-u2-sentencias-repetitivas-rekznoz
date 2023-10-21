from src.main12 import contar_letra_en_frase

def test_contar_letra_en_frase():
    assert contar_letra_en_frase("Hola mundo", "o") == 2
    assert contar_letra_en_frase("rafael", "a") == 2
    assert contar_letra_en_frase("tremenda prueba", "z") == 0
    assert contar_letra_en_frase("experto", "x") == 1