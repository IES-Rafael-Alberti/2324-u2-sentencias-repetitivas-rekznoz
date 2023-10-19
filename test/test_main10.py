from src.main10 import tipo_pizza, ingredientes_pizza

def test_tipo_pizza():
    assert tipo_pizza("vegetariana") == True
    assert tipo_pizza("no vegetariana") == False
    assert tipo_pizza("vegana") == False

def test_ingredientes_pizza():
    assert ingredientes_pizza(True, "pimiento") == True
    assert ingredientes_pizza(True, "tofu") == True
    assert ingredientes_pizza(True, "peperoni") == False
    assert ingredientes_pizza(False, "pimiento") == False
    assert ingredientes_pizza(False, "peperoni") == True
    assert ingredientes_pizza(False, "jamon") == True
    assert ingredientes_pizza(False, "salmon") == True
    assert ingredientes_pizza(True, "queso") == False