from src.main10 import es_numero_primo

def test_es_numero_primo():
    assert es_numero_primo(2) == True
    assert es_numero_primo(3) == True
    assert es_numero_primo(17) == True
    assert es_numero_primo(20) == False
    assert es_numero_primo(29) == True
    assert es_numero_primo(1) == False
    assert es_numero_primo(0) == False