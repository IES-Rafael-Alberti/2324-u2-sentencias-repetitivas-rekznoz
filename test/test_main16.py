from src.main16 import numeros_enteros

def test_numeros_enteros_numero_mayor():
    assert numeros_enteros(5, 3) == 5
    assert numeros_enteros(3, 3) == 3
    assert numeros_enteros(2, 4) == 4
    assert numeros_enteros(-1, 5) == 5
    assert numeros_enteros(0, 7) == 7