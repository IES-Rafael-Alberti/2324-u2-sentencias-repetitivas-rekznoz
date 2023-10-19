from src.main3 import numeros_impares_hasta

def test_numeros_impares_hasta():
    assert numeros_impares_hasta(5) == ["1", "3", "5"]
    assert numeros_impares_hasta(10) == ["1", "3", "5", "7", "9"]
    assert numeros_impares_hasta(1) == ["1"]
    assert numeros_impares_hasta(-5) == []