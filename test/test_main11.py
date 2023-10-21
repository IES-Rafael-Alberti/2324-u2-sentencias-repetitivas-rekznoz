from src.main11 import letras_invertidas

def test_letras_invertidas():
    assert letras_invertidas("hola") == "aloh"
    assert letras_invertidas("python") == "nohtyp"
    assert letras_invertidas("abcdefg") == "gfedcba"