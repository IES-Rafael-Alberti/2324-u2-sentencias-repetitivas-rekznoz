from src.main23 import contar_digitos_en_linea

def test_contar_digitos_en_linea_sin_digitos():
    assert contar_digitos_en_linea("Libro sin dígitos") == 0
    assert contar_digitos_en_linea("Título con 123 dígitos") == 3
    assert contar_digitos_en_linea("¡1234@#$%^&*()!") == 4