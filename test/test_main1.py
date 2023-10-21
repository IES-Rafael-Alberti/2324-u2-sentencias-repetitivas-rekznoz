from src.main1 import repetir_palabra

def test_repetir_palabra():
    assert repetir_palabra("hola", 3) == "holaholahola"
    assert repetir_palabra("nada", 0) == ""
    assert repetir_palabra("programa", 1) == "programa"