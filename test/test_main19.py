from src.main19 import load_menu

def test_load_menu():
    assert load_menu("1") == 1
    assert load_menu("2") == 2
    assert load_menu("3") == 3
    assert load_menu("99") == 0