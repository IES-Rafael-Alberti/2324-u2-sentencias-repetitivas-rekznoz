from src.main6 import crear_triangulo

def test_crear_triangulo():
    assert crear_triangulo(1) == "*\n"
    assert crear_triangulo(2) == "*\n**\n"
    assert crear_triangulo(3) == "*\n**\n***\n"
    assert crear_triangulo(0) == ""