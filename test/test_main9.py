from src.main9 import validar_contrasena

def test_validar_contrasena():
    assert validar_contrasena("pass1234","pass1234") == True
    assert validar_contrasena("pass1234","contrasena123") == False