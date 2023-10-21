from src.main4 import cuenta_atras_desde

def test_cuenta_atras_desde():
    assert cuenta_atras_desde(5) == ["5", "4", "3", "2", "1", "0"]
    assert cuenta_atras_desde(10) == ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]
    assert cuenta_atras_desde(1) == ["1", "0"]
    assert cuenta_atras_desde(-5) == []