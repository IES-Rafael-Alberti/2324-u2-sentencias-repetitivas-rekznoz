from src.main8 import generar_triangulo

def test_generar_triangulo():
    assert generar_triangulo(1) == "1\n"
    assert generar_triangulo(3) == "1\n\n3 1\n"
    assert generar_triangulo(5) == "1\n\n3 1\n\n5 3 1\n"
    assert generar_triangulo(7) == "1\n\n3 1\n\n5 3 1\n\n7 5 3 1\n"