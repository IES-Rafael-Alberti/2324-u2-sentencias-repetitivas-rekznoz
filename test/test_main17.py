from src.main17 import suma_digitos

def test_suma_digitos_un_digito():
    assert suma_digitos(5) == 5
    assert suma_digitos(12345) == 15
    assert suma_digitos(0) == 0
    assert suma_digitos(-123) == 0