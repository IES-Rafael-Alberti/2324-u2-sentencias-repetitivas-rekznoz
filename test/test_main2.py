from src.main2 import anos_cumplidos

def test_anos_cumplidos():
    assert anos_cumplidos(5) == ["1", "2", "3", "4", "5"]
    assert anos_cumplidos(1) == ["1"]
    assert anos_cumplidos(0) == []