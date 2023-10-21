from src.main21 import calcular_total_compras

def test_calcular_total_compras():
    assert calcular_total_compras([500, 300, 200]) == 1000.0
    assert calcular_total_compras([100, 200, 300, 400, 150]) == 1035.0
    assert calcular_total_compras([1000, 200, 300]) == 1350.0