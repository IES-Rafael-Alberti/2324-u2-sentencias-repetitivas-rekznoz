from src.main24 import es_primo

def test_es_primo_primos():
    assert es_primo(2) == True
    assert es_primo(1) == False
    assert es_primo(5) == True
    assert es_primo(9) == False
    assert es_primo(13) == True
