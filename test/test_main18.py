from src.main18 import suma_digitos

def test_suma_digitos_un_digito():
    assert suma_digitos(5) == 5
    assert suma_digitos(123456) == 21
    assert suma_digitos(0) == 0
    assert suma_digitos(-888) == 0