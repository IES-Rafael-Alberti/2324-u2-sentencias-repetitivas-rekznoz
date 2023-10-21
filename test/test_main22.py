from src.main22 import contar_pares_impares

def test_contar_pares_impares():
    assert contar_pares_impares(1234567890) == (5, 5)
    assert contar_pares_impares(24680) == (5, 0)
    assert contar_pares_impares(13579) == (0, 5)