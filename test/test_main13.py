from src.main13 import concatenar_frase

# Pruebas para la función concatenar_frase
def test_concatenar_frase_basico():
    assert concatenar_frase("mundo", "Hola,") == "Hola,mundo "
    assert concatenar_frase("Python", "") == "Python "
    assert concatenar_frase("!", "¡Hola") == "¡Hola! "
    frase = "Este es un ejemplo."
    frase = concatenar_frase("brutal", frase)
    frase = concatenar_frase("frase", frase)
    frase = concatenar_frase("junta", frase)
    assert frase == "Este es un ejemplo.brutal frase junta "