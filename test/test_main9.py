from src.main9 import calcular_precio_entrada

def test_calcular_precio_entrada():
    assert calcular_precio_entrada(2) == 0
    assert calcular_precio_entrada(5) == 5
    assert calcular_precio_entrada(12) == 5
    assert calcular_precio_entrada(25) == 10