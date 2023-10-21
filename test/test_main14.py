from src.main14 import sumas_enteros

def test_sumas_enteros_suma_cero():
    assert sumas_enteros(0, 0) == 0
    assert sumas_enteros(5, 10) == 15
    assert sumas_enteros(-3, 7) == 4
