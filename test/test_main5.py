from src.main5 import calcular_capital_inversion

def test_calcular_capital_inversion():
    assert calcular_capital_inversion(1000, 0.05, 3) == [1050.0, 1102.5, 1157.62]
    assert calcular_capital_inversion(5000, 0.03, 5) == [5150.0, 5304.5, 5463.64, 5627.54, 5796.37]
    assert calcular_capital_inversion(2000, 0.08, 10) == [2160.0, 2332.8, 2519.42, 2720.98, 2938.66, 3173.75, 3427.65, 3701.86, 3998.01, 4317.85]
