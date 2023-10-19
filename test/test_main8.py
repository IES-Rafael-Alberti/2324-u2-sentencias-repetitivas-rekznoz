from src.main8 import rendimiento, beneficios

def test_determinar_rendimiento():
    assert rendimiento(0.0) == "Inaceptable"
    assert rendimiento(0.4) == "Aceptable"
    assert rendimiento(0.6) == "Meritorio"

def test_calcular_beneficios():
    assert beneficios(0.0) == 0
    assert beneficios(0.4) == 960
    assert beneficios(0.6) == 1440