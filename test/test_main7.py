from src.main7 import tipo_impositivo

def test_calcular_tipo_impositivo():
    assert tipo_impositivo(5000) == 5
    assert tipo_impositivo(15000) == 15
    assert tipo_impositivo(25000) == 20
    assert tipo_impositivo(40000) == 30
    assert tipo_impositivo(70000) == 45