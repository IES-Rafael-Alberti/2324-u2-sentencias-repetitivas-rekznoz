from src.main6 import obtener_grupo

def test_obtener_grupo():
    assert obtener_grupo("Maria", "mujer") == "B"
    assert obtener_grupo("Gustavo", "hombre") == "B"
    assert obtener_grupo("Camila", "mujer") == "A"
    assert obtener_grupo("Pedro", "hombre") == "A"
    assert obtener_grupo("Andrea", "mujer") == "A"
    assert obtener_grupo("Juanillo", "hombre") == "B"